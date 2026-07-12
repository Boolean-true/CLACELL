import pandas as pd
import scipy.stats as stats
from scipy.sparse import csr_matrix
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV

from .test_robustness import test_robustness


class CellClassifier:
    def __init__(self):
        """
        Initializes the cell classififer.
        """
        self.model = None
        self.best_params_ = None
        self.is_trained = False
        self.genes_in_training_set = None
    
    # Build Pipelines with ColumnTransformer
    def _make_pipeline(self, features_to_keep, model_name, model):
        preprocessor = ColumnTransformer(
            transformers=[('keep', 'passthrough', features_to_keep)],
            remainder='drop'
        )
        return Pipeline([
            ('select', preprocessor),
            (model_name, model)
        ])

    def grid_search(
        self,
        X_train,
        y_train,
        X_test=None,
        y_test=None,
        labels="scumi-annotation",
        n_jobs=1,
    ):
        """
        Executes a hyperparameter tuning on the training set and returns the score on the test set.
        Automatically followed by a final training with the best parameters.
        """
        if not isinstance(X_train, pd.DataFrame):
            raise ValueError("X_train must be a pandas DataFrame.")

        # Train a Random Forest Classifier to get feature importances
        rf = RandomForestClassifier()
        rf.fit(X_train, y_train)
        feature_importance = rf.feature_importances_
        feature_importance = np.argsort(feature_importance)[::-1]
        sorted_top_genes = X_train.columns[feature_importance].tolist() 

        # For faster RandomSearch, convert the DataFrame to a sparse matrix
        X_sparse = csr_matrix(X_train.values)

        # Train the LinearSVC model on the training set
        base_model = LinearSVC()

        param_distribution = {
            "C": stats.loguniform(1e-3, 2.0),
            "penalty": ['l1', 'l2'],
            "dual": [True, False],
            "class_weight": ["balanced", None],
            "tol": stats.loguniform(1e-4, 1e-2),
        }

        random_search = RandomizedSearchCV(
            estimator=base_model,
            param_distributions=param_distribution,
            n_iter=50,
            cv=3,
            scoring="accuracy",
            n_jobs=n_jobs,
            verbose=10,
        )
        random_search.fit(X_sparse, y_train)

        self.best_params_ = random_search.best_params_
        print(f"Best parameters found: {self.best_params_}")

        # Create custom ensemble model
        total_genes = len(sorted_top_genes)

        # Define subsets
        drop_075_pct = int(total_genes * 0.0075)
        drop_15_pct = int(total_genes * 0.015)
        drop_25_pct = int(total_genes * 0.025)

        # Compute Features for each subset
        features_model_all = sorted_top_genes
        features_model_minus_075 = sorted_top_genes[drop_075_pct:]
        features_model_minus_15 = sorted_top_genes[drop_15_pct:]
        features_model_minus_25 = sorted_top_genes[drop_25_pct:]

        model = CalibratedClassifierCV(LinearSVC(**self.best_params_))

        pipe_all = self._make_pipeline(features_model_all, 'linsvc_all', model)
        pipe_minus_075 = self._make_pipeline(features_model_minus_075, 'linsvc_075', model)
        pipe_minus_15 = self._make_pipeline(features_model_minus_15, 'linsvc_15', model)
        pipe_minus_25 = self._make_pipeline(features_model_minus_25, 'linsvc_25', model)

        # Train Voting Classifier
        ensemble = VotingClassifier(
            estimators=[
                ('all_features', pipe_all),
                ('minus_075_pct', pipe_minus_075),
                ('minus_15_pct', pipe_minus_15),
                ('minus_25_pct', pipe_minus_25)
            ],
            voting='soft'
        )

        ensemble.fit(X_train, y_train)

        self.model = ensemble
        self.is_trained = True
        self.genes_in_training_set = X_train.columns.tolist()

        if X_test is not None and y_test is not None:
            # Compute Robustness score on test set with best parameters
            self.evaluate(X_test, y_test, labels=labels)

            # Automatically call train with best parameters on complete dataset after grid search
            print(
                "\nStart final training with best parameters on complete training data..."
            )
            X = pd.concat([X_train, X_test], axis=0, ignore_index=True)
            y = pd.concat([y_train, y_test], axis=0, ignore_index=True)
            self.train(X, y, **self.best_params_)

    def train(
        self, X_train, y_train, **hyperparameters
    ):
        """
        Trains the model one the complete dataset with the given hyperparameters.
        Can be either called automatically after grid search or manually with custom hyperparameters.
        """
        if not isinstance(X_train, pd.DataFrame):
            raise ValueError("X_train must be a pandas DataFrame.")
        
        # Train a Random Forest Classifier to get feature importances
        rf = RandomForestClassifier()
        rf.fit(X_train, y_train)
        feature_importance = rf.feature_importances_
        feature_importance = np.argsort(feature_importance)[::-1]
        sorted_top_genes = X_train.columns[feature_importance].tolist() 

        print(f"Train models with parameters: {hyperparameters}")

        # Create custom ensemble model
        total_genes = len(sorted_top_genes)

        # Define subsets
        drop_075_pct = int(total_genes * 0.0075)
        drop_15_pct = int(total_genes * 0.015)
        drop_25_pct = int(total_genes * 0.025)

        # Compute Features for each subset
        features_model_all = sorted_top_genes
        features_model_minus_075 = sorted_top_genes[drop_075_pct:]
        features_model_minus_15 = sorted_top_genes[drop_15_pct:]
        features_model_minus_25 = sorted_top_genes[drop_25_pct:]

        model = CalibratedClassifierCV(LinearSVC(**hyperparameters))

        pipe_all = self._make_pipeline(features_model_all, 'linsvc_all', model)
        pipe_minus_075 = self._make_pipeline(features_model_minus_075, 'linsvc_075', model)
        pipe_minus_15 = self._make_pipeline(features_model_minus_15, 'linsvc_15', model)
        pipe_minus_25 = self._make_pipeline(features_model_minus_25, 'linsvc_25', model)

        # Train Voting Classifier
        ensemble = VotingClassifier(
            estimators=[
                ('all_features', pipe_all),
                ('minus_075_pct', pipe_minus_075),
                ('minus_15_pct', pipe_minus_15),
                ('minus_25_pct', pipe_minus_25)
            ],
            voting='soft'
        )

        ensemble.fit(X_train, y_train)

        self.model = ensemble
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
                "The model wasn't trained yet. Call 'train' or 'grid_search' first."
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
                "The model wasn't trained yet. Call 'train' or 'grid_search' first."
            )

        # Filter genes that are not in the training set and reorder the remaining genes to match the training set
        X = X.reindex(columns=self.genes_in_training_set, fill_value=0)

        print("Infer new data...")
        return self.model.predict(X)
