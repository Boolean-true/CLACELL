import pandas as pd
import scipy.stats as stats
from scipy.sparse import csr_matrix
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

    def grid_search(self, X_train, y_train, X_test=None, y_test=None, adata=None, val_size=0.2, n_jobs=1):
        """
        Executes a hyperparameter tuning on the training set and returns the score on the test set.
        Automatically followed by a final training with the best parameters.
        """
        # Split the training data into training and validation sets
        if X_test is None or y_test is None:
            print("No test set provided. Splitting training data into training and validation sets...")
            X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=val_size)
        
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
        self.model=tuned_classifier.best_estimator_
        self.best_params_ = tuned_classifier.best_params_
        self.is_trained = True

        # Compute Robustness score on test set with best parameters
        #TODO: feature importance and out of distribution are missing
        self.evaluate(X_test, y_test)
        
        # Automatically call train with best parameters on complete dataset after grid search
        print("\nStart final training with best parameters on complete training data...")
        X = pd.concat([X_train, X_test], axis=0, ignore_index=True)
        y = pd.concat([y_train, y_test], axis=0, ignore_index=True)
        self.train(X, y, adata=adata, **self.best_params_)

    def train(self, X_train, y_train, adata=None, **hyperparameters):
        """
        Trains the model one the complete dataset with the given hyperparameters.
        Can be either called automatically after grid search or manually with custom hyperparameters.
        """
        print(f"Train models with parameters: {hyperparameters}")

        self.model = LogisticRegression(**hyperparameters)
        self.model.fit(X_train, y_train)
        self.is_trained = True

    def evaluate(self, X_test, y_test, ood_dataset_path=None, feature_importances=None):
        """
        Evaluates the model on the test set and returns the score.
        If the model is not trained yet, it raises an error.
        """
        if not self.is_trained:
            raise RuntimeError("The model wasn't trained yet. Call 'train' or 'grid_search' first.")
        
        print("Evaluate model on test data...")
        test_robustness(self.model, X_test, y_test, ood_dataset_path, feature_importances)

    def predict(self, X):
        """
        Infers new data with the trained model and returns the labels.
        If the model is not trained yet, it raises an error.
        """
        if not self.is_trained:
            raise RuntimeError("The model wasn't trained yet. Call 'train' or 'grid_search' first.")
        
        print("Infer new data...")
        return self.model.predict(X)
