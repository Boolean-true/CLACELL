import pandas as pd
import scipy.stats as stats
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import OneHotEncoder
from sklearn.svm import LinearSVC
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from skopt import BayesSearchCV
from skopt.space import Integer, Real, Categorical

from .test_robustness import test_robustness
from .custom_stopper import CustomStopper


class ConditionalDAE(nn.Module):
    def __init__(self, input_dim, num_donors, latent_dim=128, noise_factor=0.3):
        super(ConditionalDAE, self).__init__()

        self.noise_factor = noise_factor

        self.encoder = nn.Sequential(
            nn.Linear(input_dim + num_donors, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(256, latent_dim)
        )

        self.decoder = nn.Sequential(
            nn.Linear(latent_dim + num_donors, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(256, input_dim)
        )

    def forward(self, x, cond):
        if self.training:
            noise = torch.randn_like(x) * self.noise_factor
            x_noisy = x + noise
        else:
            x_noisy = x

        # Combine Gene data and Donor ID for the Encoder
        x_cond = torch.cat([x_noisy, cond], dim=1)
        latent = self.encoder(x_cond)

        # Combine Latent space and Donor ID for the Decoder
        latent_cond = torch.cat([latent, cond], dim=1)
        reconstructed = self.decoder(latent_cond)

        return reconstructed, latent


class ScRNACVAEClassifier:
    def __init__(self, cdae, classifier, scaler, num_donors):
        self.cdae = cdae
        self.classifier = classifier
        self.scaler = scaler
        self.num_donors = num_donors
        self.cdae.eval()
        self.device = next(cdae.parameters()).device

    def _transform_to_latent(self, X):
        if hasattr(X, "toarray"):
            X = X.toarray()
        if self.scaler is not None:
            X = self.scaler.transform(X)
            
        X_tensor = torch.tensor(X, dtype=torch.float32).to(self.device)
        
        cond_dummy = torch.zeros((X_tensor.shape[0], self.num_donors), dtype=torch.float32).to(self.device)
        
        with torch.no_grad():
            _, latent_tensor = self.cdae(X_tensor, cond_dummy)
            X_latent = latent_tensor.cpu().numpy()
            
        return X_latent

    def predict(self, X):
        X_latent = self._transform_to_latent(X)
        return self.classifier.predict(X_latent)

    def predict_proba(self, X):
        X_latent = self._transform_to_latent(X)
        return self.classifier.predict_proba(X_latent)


class ConditionalCellClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, n_iter_search=30, random_state=None):
        """
        Initializes the cell classififer.
        """
        self.n_iter_search = n_iter_search
        self.random_state = random_state

        self.model = None
        self.best_params_ = None
        self.is_trained = False
        self.genes_in_training_set = None

    def random_search(
        self,
        X_train,
        y_train,
        donor_train,
        X_test=None,
        y_test=None,
        donor_test=None,
        labels="scumi-annotation",
        n_jobs=1,
    ):
        """
        Executes a hyperparameter tuning on the training set and returns the score on the test set.
        Automatically followed by a final training with the best parameters.
        """
        if not isinstance(X_train, pd.DataFrame):
            raise ValueError("X_train must be a pandas DataFrame.")

        if not isinstance(donor_train, pd.Series):
            raise ValueError("donor_train must be a pandas Series.")

        if X_test is not None:
            if not isinstance(X_test, pd.DataFrame):
                raise ValueError("X_test must be a pandas DataFrame.")
            if y_test is None:
                raise ValueError("y_test must be provided if X_test is provided.")
            if donor_test is None:
                raise ValueError("donor_test must be provided if X_test is provided.")
            if not isinstance(donor_test, pd.Series):
                raise ValueError("donor_test must be a pandas Series.")

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        if hasattr(X_train, "toarray"):
            X_train = X_train.toarray()
        if X_test is not None and hasattr(X_test, "toarray"):
            X_test = X_test.toarray()

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)

        oh_encoder = OneHotEncoder(sparse_output=False)
        donor_train_oh = oh_encoder.fit_transform(donor_train.to_numpy().reshape(-1, 1))

        num_donors = donor_train_oh.shape[1]
        input_dim = X_train_scaled.shape[1]
        latent_dim = 128

        # Train DAE
        input_dim = X_train_scaled.shape[1]
        cdae = ConditionalDAE(input_dim, num_donors, latent_dim).to(device)

        criterion = nn.MSELoss()
        optimizer = optim.AdamW(cdae.parameters(), lr=1e-3, weight_decay=1e-4)

        train_dataset = TensorDataset(
            torch.tensor(X_train_scaled, dtype=torch.float32),
            torch.tensor(donor_train_oh, dtype=torch.float32)
        )
        train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True)


        num_epochs = 150
        best_loss = float('inf')
        patience_counter = 0
        patience = 5
        delta_loss = 0.0002
        cdae.train()

        print("Start Conditional DAE Training...")
        for epoch in range(num_epochs):
            epoch_loss = 0.0
            for x_batch, cond_batch in train_loader:
                x_batch = x_batch.to(device)
                cond_batch = cond_batch.to(device)

                optimizer.zero_grad()
                reconstructed, latent = cdae(x_batch, cond_batch)

                loss = criterion(reconstructed, x_batch)
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item() * x_batch.size(0)
                
            total_epoch_loss = epoch_loss / len(train_loader.dataset)
            if (epoch + 1) % 10 == 0 or epoch == 0:
                print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {total_epoch_loss:.4f}")
            
            # Early Stopping
            if total_epoch_loss < best_loss - delta_loss:
                best_loss = total_epoch_loss
                patience_counter = 0
            else:
                patience_counter += 1

            if patience_counter >= patience:
                print(f"Early Stopping after [{epoch+1}/{num_epochs}] Epochs!")
                break
        
        cdae.eval()
        print("\nExtract robust features...")
        with torch.no_grad():
            # Prepare training data for latent space extraction
            X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32).to(device)
            cond_train_tensor = torch.tensor(donor_train_oh, dtype=torch.float32).to(device)
            _, X_train_latent_tensor = cdae(X_train_tensor, cond_train_tensor)
            X_train_latent = X_train_latent_tensor.cpu().numpy()

        print("Start Hyperparametertuning...")
        base_model = LinearSVC(random_state=self.random_state)

        param_distributions = {
                'C': stats.loguniform(1e-3, 2.0),
                'penalty': ['l2'],
                'dual': [True, False],
                'class_weight': ['balanced', None],
                'tol': stats.loguniform(1e-3, 1e-1)
            }
        random_search = RandomizedSearchCV(
            estimator=base_model,
            param_distributions=param_distributions,
            n_iter=self.n_iter_search,
            cv=5,
            scoring='accuracy',
            n_jobs=n_jobs,
            verbose=10
        )
        random_search.fit(X_train_latent, y_train)

        self.best_params_ = random_search.best_params_
        print(f"Best parameters found: {self.best_params_}")
        best_model = random_search.best_estimator_

        robust_model = ScRNACVAEClassifier(
            cdae=cdae,
            classifier=best_model,
            scaler=scaler,
            num_donors=num_donors
        )

        self.model = robust_model
        self.is_trained = True
        self.genes_in_training_set = X_train.columns.tolist()

        if X_test is not None and y_test is not None:
            # Compute Robustness score on test set with best parameters
            self.evaluate(X_test, y_test, labels=labels)

            # Automatically call train with best parameters on complete dataset after random search
            print(
                "\nStart final training with best parameters on complete training data..."
            )
            X = pd.concat([X_train, X_test], axis=0, ignore_index=True)
            y = pd.concat([y_train, y_test], axis=0, ignore_index=True)
            donors = pd.concat([donor_train, donor_test], axis=0, ignore_index=True)
            self.train(X, y, donors, **self.best_params_)

    def bayes_search(
        self,
        X_train,
        y_train,
        donor_train,
        X_test=None,
        y_test=None,
        donor_test=None,
        labels="scumi-annotation",
        n_jobs=1,
    ):
        """
        Executes a hyperparameter tuning on the training set and returns the score on the test set.
        Automatically followed by a final training with the best parameters.
        """
        if not isinstance(X_train, pd.DataFrame):
            raise ValueError("X_train must be a pandas DataFrame.")

        if not isinstance(donor_train, pd.Series):
            raise ValueError("donor_train must be a pandas Series.")

        if X_test is not None:
            if not isinstance(X_test, pd.DataFrame):
                raise ValueError("X_test must be a pandas DataFrame.")
            if y_test is None:
                raise ValueError("y_test must be provided if X_test is provided.")
            if donor_test is None:
                raise ValueError("donor_test must be provided if X_test is provided.")
            if not isinstance(donor_test, pd.Series):
                raise ValueError("donor_test must be a pandas Series.")

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        if hasattr(X_train, "toarray"):
            X_train = X_train.toarray()
        if X_test is not None and hasattr(X_test, "toarray"):
            X_test = X_test.toarray()

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)

        oh_encoder = OneHotEncoder(sparse_output=False)
        donor_train_oh = oh_encoder.fit_transform(donor_train.to_numpy().reshape(-1, 1))

        num_donors = donor_train_oh.shape[1]
        input_dim = X_train_scaled.shape[1]
        latent_dim = 128

        # Train DAE
        input_dim = X_train_scaled.shape[1]
        cdae = ConditionalDAE(input_dim, num_donors, latent_dim).to(device)

        criterion = nn.MSELoss()
        optimizer = optim.AdamW(cdae.parameters(), lr=1e-3, weight_decay=1e-4)

        train_dataset = TensorDataset(
            torch.tensor(X_train_scaled, dtype=torch.float32),
            torch.tensor(donor_train_oh, dtype=torch.float32)
        )
        train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True)


        num_epochs = 150
        best_loss = float('inf')
        patience_counter = 0
        patience = 5
        delta_loss = 0.0002
        cdae.train()

        print("Start Conditional DAE Training...")
        for epoch in range(num_epochs):
            epoch_loss = 0.0
            for x_batch, cond_batch in train_loader:
                x_batch = x_batch.to(device)
                cond_batch = cond_batch.to(device)

                optimizer.zero_grad()
                reconstructed, latent = cdae(x_batch, cond_batch)

                loss = criterion(reconstructed, x_batch)
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item() * x_batch.size(0)
                
            total_epoch_loss = epoch_loss / len(train_loader.dataset)
            if (epoch + 1) % 10 == 0 or epoch == 0:
                print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {total_epoch_loss:.4f}")
            
            # Early Stopping
            if total_epoch_loss < best_loss - delta_loss:
                best_loss = total_epoch_loss
                patience_counter = 0
            else:
                patience_counter += 1

            if patience_counter >= patience:
                print(f"Early Stopping after [{epoch+1}/{num_epochs}] Epochs!")
                break
        
        cdae.eval()
        print("\nExtract robust features...")
        with torch.no_grad():
            # Prepare training data for latent space extraction
            X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32).to(device)
            cond_train_tensor = torch.tensor(donor_train_oh, dtype=torch.float32).to(device)
            _, X_train_latent_tensor = cdae(X_train_tensor, cond_train_tensor)
            X_train_latent = X_train_latent_tensor.cpu().numpy()

        print("Start Hyperparametertuning...")
        base_model = LinearSVC(random_state=self.random_state)

        param_distributions = {
                'C': Real(1e-3, 2.0, prior='log-uniform'),
                'penalty': Categorical(['l2']),
                'dual': Categorical([True, False]),
                'class_weight': Categorical(['balanced', None]),
                'tol': Real(1e-3, 1e-1, prior='log-uniform')
            }
        my_stopper = CustomStopper(patience=5, min_delta=0.002, min_iter=15)
        opt = BayesSearchCV(
                    estimator=base_model,
                    search_spaces=param_distributions,
                    n_iter=self.n_iter_search,
                    cv=5,
                    scoring='accuracy',
                    n_jobs=n_jobs,
                    verbose=10
                )
        opt.fit(X_train_latent, y_train, callback=my_stopper)

        print(f"\nSearch terminated after {len(opt.cv_results_['mean_test_score'])} Iterations.")
        self.best_params_ = opt.best_params_
        print(f"Best parameters found: {self.best_params_}")
        best_model = opt.best_estimator_

        robust_model = ScRNACVAEClassifier(
            cdae=cdae,
            classifier=best_model,
            scaler=scaler,
            num_donors=num_donors
        )

        self.model = robust_model
        self.is_trained = True
        self.genes_in_training_set = X_train.columns.tolist()

        if X_test is not None and y_test is not None:
            # Compute Robustness score on test set with best parameters
            self.evaluate(X_test, y_test, labels=labels)

            # Automatically call train with best parameters on complete dataset after random search
            print(
                "\nStart final training with best parameters on complete training data..."
            )
            X = pd.concat([X_train, X_test], axis=0, ignore_index=True)
            y = pd.concat([y_train, y_test], axis=0, ignore_index=True)
            donors = pd.concat([donor_train, donor_test], axis=0, ignore_index=True)
            self.train(X, y, donors, **self.best_params_)

    def train(
        self, X_train, y_train, donor_train, **hyperparameters
    ):
        """
        Trains the model one the complete dataset with the given hyperparameters.
        Can be either called automatically after random search or manually with custom hyperparameters.
        """
        if not isinstance(X_train, pd.DataFrame):
            raise ValueError("X_train must be a pandas DataFrame.")

        if not isinstance(donor_train, pd.Series):
            raise ValueError("donor_train must be a pandas Series.")

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        if hasattr(X_train, "toarray"):
            X_train = X_train.toarray()

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)

        oh_encoder = OneHotEncoder(sparse_output=False)
        donor_train_oh = oh_encoder.fit_transform(donor_train.to_numpy().reshape(-1, 1))

        num_donors = donor_train_oh.shape[1]
        input_dim = X_train_scaled.shape[1]
        latent_dim = 128

        # Train DAE
        input_dim = X_train_scaled.shape[1]
        cdae = ConditionalDAE(input_dim, num_donors, latent_dim).to(device)

        criterion = nn.MSELoss()
        optimizer = optim.AdamW(cdae.parameters(), lr=1e-3, weight_decay=1e-4)

        train_dataset = TensorDataset(
            torch.tensor(X_train_scaled, dtype=torch.float32),
            torch.tensor(donor_train_oh, dtype=torch.float32)
        )
        train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True)


        num_epochs = 150
        best_loss = float('inf')
        patience_counter = 0
        patience = 5
        delta_loss = 0.0002
        cdae.train()

        print("Start Conditional DAE Training...")
        for epoch in range(num_epochs):
            epoch_loss = 0.0
            for x_batch, cond_batch in train_loader:
                x_batch = x_batch.to(device)
                cond_batch = cond_batch.to(device)

                optimizer.zero_grad()
                reconstructed, latent = cdae(x_batch, cond_batch)

                loss = criterion(reconstructed, x_batch)
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item() * x_batch.size(0)
                
            total_epoch_loss = epoch_loss / len(train_loader.dataset)
            if (epoch + 1) % 10 == 0 or epoch == 0:
                print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {total_epoch_loss:.4f}")
            
            # Early Stopping
            if total_epoch_loss < best_loss - delta_loss:
                best_loss = total_epoch_loss
                patience_counter = 0
            else:
                patience_counter += 1

            if patience_counter >= patience:
                print(f"Early Stopping after [{epoch+1}/{num_epochs}] Epochs!")
                break
        
        cdae.eval()
        print("\nExtract robust features...")
        with torch.no_grad():
            # Prepare training data for latent space extraction
            X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32).to(device)
            cond_train_tensor = torch.tensor(donor_train_oh, dtype=torch.float32).to(device)
            _, X_train_latent_tensor = cdae(X_train_tensor, cond_train_tensor)
            X_train_latent = X_train_latent_tensor.cpu().numpy()


        base_model = LinearSVC(random_state=self.random_state, **hyperparameters)
        base_model.fit(X_train_latent, y_train)
        robust_model = ScRNACVAEClassifier(
            cdae=cdae,
            classifier=base_model,
            scaler=scaler,
            num_donors=num_donors
        )

        self.model = robust_model
        self.is_trained = True
        self.genes_in_training_set = X_train.columns.tolist()

    def evaluate(
        self,
        X_test,
        y_test,
        labels="scumi-annotation",
        X_ood=None,
        y_ood=None,
        feature_importances=None,
        log_to_console=True,
        log_to_file=True,
    ):
        """
        Evaluates the model on the test set and returns the score.
        If the model is not trained yet, it raises an error.
        """
        if not self.is_trained:
            raise RuntimeError(
                "The model wasn't trained yet. Call 'train' or 'random_search' first."
            )

        print("Evaluate model on test data...")
        return test_robustness(
            self.model,
            X_test,
            y_test,
            labels,
            X_ood,
            y_ood,
            feature_importances,
            log_to_console=log_to_console,
            log_to_file=log_to_file,
        )

    def predict(self, X):
        """
        Infers new data with the trained model and returns the labels.
        If the model is not trained yet, it raises an error.
        """
        if not isinstance(X, pd.DataFrame):
            raise ValueError("X must be a pandas DataFrame.")

        if not self.is_trained:
            raise RuntimeError(
                "The model wasn't trained yet. Call 'train' or 'random_search' first."
            )

        # Filter genes that are not in the training set and reorder the remaining genes to match the training set
        X = X.reindex(columns=self.genes_in_training_set, fill_value=0)

        print("Infer new data...")
        return self.model.predict(X)
