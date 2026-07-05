import pandas as pd
import scipy.stats as stats
from scipy.sparse import csr_matrix
import anndata as ad
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV

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

    def grid_search(
        self,
        X_train,
        y_train=None,
        X_test=None,
        y_test=None,
        labels="scumi-annotation",
        val_size=0.25,
        n_jobs=1,
    ):
        """
        Executes a hyperparameter tuning on the training set and returns the score on the test set.
        Automatically followed by a final training with the best parameters.
        """
        # Prepare the data for training and testing
        if isinstance(X_train, ad.AnnData):
            # X_train is an AnnData object
            X = X_train.to_df()
            y = X_train.obs[labels]
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=val_size
            )
        else:
            # X_train is a DataFrame -> check if y_train and test split are provided
            if y_train is None:
                raise ValueError(
                    "y_train must be provided if X_train is not an AnnData object."
                )

            if X_test is None or y_test is None:
                # Split the training data into training and validation sets
                X_train, X_test, y_train, y_test = train_test_split(
                    X_train, y_train, test_size=val_size
                )

        # For faster RandomSearch, convert the DataFrame to a sparse matrix
        X_sparse = csr_matrix(X_train.values)

        base_logreg = LogisticRegression()

        param_distributions = {
            "solver": ["saga"],
            "max_iter": [1000],
            "C": stats.loguniform(1e-3, 2.0),
            "l1_ratio": [0.0, 0.25, 0.5, 0.75, 1.0],
            "class_weight": ["balanced", None],
            "tol": stats.loguniform(1e-3, 1e-1),
        }

        tuned_classifier = RandomizedSearchCV(
            estimator=base_logreg,
            param_distributions=param_distributions,
            n_iter=5,
            cv=3,
            scoring="accuracy",
            n_jobs=n_jobs,
            verbose=10,
        )
        tuned_classifier.fit(X_sparse, y_train)

        self.best_params_ = tuned_classifier.best_params_
        print(f"Best parameters found: {self.best_params_}")

        # Retrain the model with the best parameters on the training set dataframe
        best_model = LogisticRegression(**self.best_params_)
        best_model.fit(X_train, y_train)
        self.model = best_model
        self.is_trained = True
        self.genes_in_training_set = X_train.columns.tolist()

        # Compute Robustness score on test set with best parameters
        self.evaluate(X_test, y_test, labels=labels)

        # Automatically call train with best parameters on complete dataset after grid search
        print(
            "\nStart final training with best parameters on complete training data..."
        )
        X = pd.concat([X_train, X_test], axis=0, ignore_index=True)
        y = pd.concat([y_train, y_test], axis=0, ignore_index=True)
        self.train(X, y, labels=labels, **self.best_params_)

    def train(
        self, X_train, y_train=None, labels="scumi-annotation", **hyperparameters
    ):
        """
        Trains the model one the complete dataset with the given hyperparameters.
        Can be either called automatically after grid search or manually with custom hyperparameters.
        """
        # Prepare the data for training and testing
        if isinstance(X_train, ad.AnnData):
            # X_train is an AnnData object
            y_train = X_train.obs[labels]
            X_train = X_train.to_df()
        else:
            # X_train is a DataFrame -> check if y_train is provided
            if y_train is None:
                raise ValueError(
                    "y_train must be provided if X_train is not an AnnData object."
                )

        print(f"Train models with parameters: {hyperparameters}")

        self.model = LogisticRegression(**hyperparameters)
        self.model.fit(X_train, y_train)
        self.is_trained = True
        self.genes_in_training_set = X_train.columns.tolist()

    def evaluate(
        self,
        X_test,
        y_test=None,
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
        # Prepare the data for training and testing
        if isinstance(X_test, ad.AnnData):
            # X_test is an AnnData object
            X_test = X_test.to_df()
            y_test = X_test.obs[labels]
        else:
            # X_test is a DataFrame -> check if y_test is provided
            if y_test is None:
                raise ValueError(
                    "y_test must be provided if X_test is not an AnnData object."
                )

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
        if isinstance(X, ad.AnnData):
            # X is an AnnData object
            X = X.to_df()

        if not self.is_trained:
            raise RuntimeError(
                "The model wasn't trained yet. Call 'train' or 'grid_search' first."
            )

        # Filter genes that are not in the training set and reorder the remaining genes to match the training set
        X = X.reindex(columns=self.genes_in_training_set, fill_value=0)

        print("Infer new data...")
        return self.model.predict(X)
