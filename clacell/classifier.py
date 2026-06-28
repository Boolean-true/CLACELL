import pandas as pd
import scipy.stats as stats
from scipy.sparse import csr_matrix
import scanpy as sc
import anndata as ad
import pandas as pd
from .test_robustness import test_robustness
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV

class BloodCellClassifier:
    def __init__(self):
        """
        Initializes the blood cell classififer.
        """
        self.model = None
        self.best_params_ = None
        self.is_trained = False

    def _preprocess_adata(self, adata):
        """
        Preprocesses the AnnData object for training and testing.
        """
        # mitochondrial genes, "MT-" for human, "Mt-" for mouse
        adata.var["mt"] = adata.var_names.str.startswith("MT-")
        # ribosomal genes
        adata.var["ribo"] = adata.var_names.str.startswith(("RPS", "RPL"))
        # hemoglobin genes
        adata.var["hb"] = adata.var_names.str.contains("^HB[^(P)]")

        sc.pp.calculate_qc_metrics(adata, qc_vars=["mt", "ribo", "hb"], inplace=True, log1p=True)

        # Remove mitochondrial, ribosomal and hemoglobin
        adata = adata[:, ~adata.var["mt"]].copy()
        adata = adata[:, ~adata.var["ribo"]].copy()
        adata = adata[:, ~adata.var["hb"]].copy()

        # Doublet Detection
        sc.pp.scrublet(adata, batch_key="Donor")
        adata = adata[adata.obs['predicted_doublet'] == False].copy()


        # Normalization

        # Saving count data
        adata.layers["counts"] = adata.X.copy()

        # Normalizing to median total counts
        sc.pp.normalize_total(adata, target_sum=1e4)
        # Logarithmize the data
        sc.pp.log1p(adata)

        # Filtering Highly variable genes
        sc.pp.highly_variable_genes(adata, n_top_genes=10000)

        # Apply filter
        adata = adata[:, adata.var['highly_variable']].copy()

        return adata

    def grid_search(self, X_train, y_train=None, X_test=None, y_test=None, val_size=0.25, n_jobs=1):
        """
        Executes a hyperparameter tuning on the training set and returns the score on the test set.
        Automatically followed by a final training with the best parameters.
        """
        # Prepare the data for training and testing
        #if hasattr(X_train, 'X') and hasattr(X_train, 'obs'):
        if isinstance(X_train, ad.AnnData):
            # X_train is an AnnData object -> preprocess it
            adata = self._preprocess_adata(X_train)
            X = adata.to_df()
            y = adata.obs['scumi-annotation']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=val_size)
        else:
            # X_train is a DataFrame -> check if y_train and test split are provided
            if y_train is None:
                raise ValueError("y_train must be provided if X_train is not an AnnData object.")

            if X_test is None or y_test is None:
                # Split the training data into training and validation sets
                X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=val_size)
        
        # For faster RandomSearch, convert the DataFrame to a sparse matrix
        X_sparse = csr_matrix(X_train.values)
        
        base_logreg = LogisticRegression()

        param_distributions = {
            'solver': ['saga'],
            'max_iter': [1000],
            'C': stats.loguniform(1e-3, 2.0),
            'l1_ratio': [0.0, 0.25, 0.5, 0.75, 1.0],
            'class_weight': ['balanced', None],
            'tol': stats.loguniform(1e-3, 1e-1)
        }

        tuned_classifier = RandomizedSearchCV(
            estimator=base_logreg,
            param_distributions=param_distributions,
            n_iter=5,#30,
            cv=3,
            scoring='accuracy',
            n_jobs=n_jobs,
            verbose=10
        )
        tuned_classifier.fit(X_sparse, y_train)

        self.best_params_ = tuned_classifier.best_params_
        print(f"Best parameters found: {self.best_params_}")

        # Retrain the model with the best parameters on the training set dataframe
        best_model = LogisticRegression(**self.best_params_)
        best_model.fit(X_train, y_train)
        self.model = best_model
        self.is_trained = True

        # Compute Robustness score on test set with best parameters
        #TODO: feature importance and out of distribution are missing
        self.evaluate(X_test, y_test)
        
        # Automatically call train with best parameters on complete dataset after grid search
        print("\nStart final training with best parameters on complete training data...")
        X = pd.concat([X_train, X_test], axis=0, ignore_index=True)
        y = pd.concat([y_train, y_test], axis=0, ignore_index=True)
        self.train(X, y, **self.best_params_)

    def train(self, X_train, y_train=None, **hyperparameters):
        """
        Trains the model one the complete dataset with the given hyperparameters.
        Can be either called automatically after grid search or manually with custom hyperparameters.
        """
        # Prepare the data for training and testing
        if isinstance(X_train, ad.AnnData):
            # X_train is an AnnData object -> preprocess it
            adata = self._preprocess_adata(X_train)
            X_train = adata.to_df()
            y_train = adata.obs['scumi-annotation']
        else:
            # X_train is a DataFrame -> check if y_train is provided
            if y_train is None:
                raise ValueError("y_train must be provided if X_train is not an AnnData object.")

        print(f"Train models with parameters: {hyperparameters}")

        self.model = LogisticRegression(**hyperparameters)
        self.model.fit(X_train, y_train)
        self.is_trained = True

    def evaluate(self, X_test, y_test=None, ood_dataset_path=None, feature_importances=None):
        """
        Evaluates the model on the test set and returns the score.
        If the model is not trained yet, it raises an error.
        """
        # Prepare the data for training and testing
        if isinstance(X_test, ad.AnnData):
            # X_test is an AnnData object -> preprocess it
            adata = self._preprocess_adata(X_test)
            X_test = adata.to_df()
            y_test = adata.obs['scumi-annotation']
        else:
            # X_test is a DataFrame -> check if y_test is provided
            if y_test is None:
                raise ValueError("y_test must be provided if X_test is not an AnnData object.")
        
        if not self.is_trained:
            raise RuntimeError("The model wasn't trained yet. Call 'train' or 'grid_search' first.")
        
        print("Evaluate model on test data...")
        test_robustness(self.model, X_test, y_test, ood_dataset_path, feature_importances)

    def predict(self, X):
        """
        Infers new data with the trained model and returns the labels.
        If the model is not trained yet, it raises an error.
        """
        if isinstance(X, ad.AnnData):
            # X is an AnnData object -> preprocess it
            adata = self._preprocess_adata(X)
            X = adata.to_df()

        if not self.is_trained:
            raise RuntimeError("The model wasn't trained yet. Call 'train' or 'grid_search' first.")
        
        print("Infer new data...")
        return self.model.predict(X)
