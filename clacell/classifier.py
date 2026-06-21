from test_robustness import test_robustness 

class BloodCellClassifier:
    def __init__(self):
        """
        Initializes the blood cell classififer.
        """
        self.model = None
        self.best_params_ = None
        self.is_trained = False

    def grid_search(self, X_train, y_train, X_test, y_test, adata=None, val_size=0.2):
        """
        Executes a hyperparameter tuning on the training set and returns the score on the test set.
        Automatically followed by a final training with the best parameters.
        """
        #TODO: Implement grid search logic here

        # Compute Robustness score on test set with best parameters
        print("\nStart robustness testing with best parameters on test data...")
        #TODO: feature importance and out of distribution are missing
        test_robustness(self.model, X_test, y_test)
        
        # Automatically call train with best parameters on complete dataset after grid search
        print("\nStart final training with best parameters on complete training data...")
        self.train(X_train, y_train, X_test, y_test, adata=adata, **self.best_params_)

    def train(self, X_train, y_train, X_test, y_test, adata=None, **hyperparameters):
        """
        Trains the model one the complete dataset with the given hyperparameters.
        Can be either called automatically after grid search or manually with custom hyperparameters.
        """
        print(f"Train models with parameters: {hyperparameters}")

        #TODO: Implement train logic here
        #TODO: Merge train and test set for final training or use adata for training if provided
        self.model = "Trained model"  # Dummy
        self.is_trained = True

    def predict(self, X):
        """
        Infers new data with the trained model and returns the labels.
        If the model is not trained yet, it raises an error.
        """
        if not self.is_trained:
            raise RuntimeError("The model wasn't trained yet. Call 'train' or 'grid_search' first.")
        
        print("Infer new data...")
        # TODO: Implement prediction logic here
        return self.model.predict(X) # Dummy
