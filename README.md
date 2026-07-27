[![DOI](https://zenodo.org/badge/1211898528.svg)](https://doi.org/10.5281/zenodo.21628448)

# CLACELL

This package includes two robust cell type classifier for immune cells. The CellClassifier has a high prediction stability with a low standard deviation of scores, while the ConditionalCellClassifier offers a higher out-of-distribution generalization at the cost of a lower prediction stability.

For a detailed example workflow, check out the [example notebook](https://github.com/Boolean-true/CLACELL/blob/main/sample_scripts/clacell_example.ipynb).

## Usage

### MarkerAnnotator

The MarkerAnnotator can be used to annotate an Anndata dataset. It uses a marker based annotation strategy to annotate the dataset. It takes only a dictionary with markers as an input.

```python
from clacell import MarkerAnnotator

annotator = MarkerAnnotator(marker_dict=marker_dict)
adata = annotator.annotate(adata)
# Now adata.obs['scumi-annotation'] contains the annotations
```

### Preprocessing

You should preprocess your data before you give it to the CellClassifier. A sample Preprocessing can be applied with the provided method preprocess_data.

```python
from clacell import preprocess_data

adata_preprocessed = preprocess_data(adata)
```

### CellClassifier

This classifier is a feature-subsampling custom ensemble using multiple LinearSVC with different amount of features as Input. It has five different methods:
1. **random_search**: Makes a search over the hyperparameters of the model, evaluates the best model and retrains it on the whole dataset using 'train'.
2. **bayes_search**: Makes a bayesian search over the hyperparameters of the model, evaluates the best model and retrains it on the whole dataset using 'train'.
3. **train**: Trains the model with the given hyperparameters.
4. **evaluate**: Evaluates the current model with robustness tests. The model needs to be trained before this method is called. The logs can be printed in the console as well as in a log file. The results will be returned in a dataframe with a multi index for easier access.
5. **predict**: Predicts new samples. The model needs to be trained before this method is called.

All methods can be called with Dataframes or with an Anndata object. Either way the data has to be processed. We recommend to use Dataframes so you can choose the train test split yourself for more realistic results. If an Anndata object is provided, the train test split will be random and won't consider batches.

```python
from clacell import CellClassifier

classifier = CellClassifier()

# 1. RandomSearch
print("\n1. random_search")
classifier.random_search(X_train, y_train, X_test, y_test, n_jobs=3)

# 2. Bayes Search
print("\n2. bayes_search")
classifier.bayes_search(X_train, y_train, X_test, y_test, n_jobs=3)

# 3. Train
print("\n3. train")
classifier.train(X_train, y_train, C=0.001)

# 4. Evaluate
print("\n4. evaluate")
classifier.evaluate(X_test, y_test, log_to_console=True, log_to_file=True)

# 5. Predict
print("\n5. predict")
predictions = classifier.predict(X_test)
print(f"Macro F1: {f1_score(y_test, predictions, average="macro")}")
```


### ConditionalCellClassifier

This classifier is a Conditional Autoencoder with a LinearSVC. It has five different methods:
1. **random_search**: Makes a search over the hyperparameters of the model, evaluates the best model and retrains it on the whole dataset using 'train'.
2. **bayes_search**: Makes a bayesian search over the hyperparameters of the model, evaluates the best model and retrains it on the whole dataset using 'train'.
3. **train**: Trains the model with the given hyperparameters.
4. **evaluate**: Evaluates the current model with robustness tests. The model needs to be trained before this method is called. The logs can be printed in the console as well as in a log file. The results will be returned in a dataframe with a multi index for easier access.
5. **predict**: Predicts new samples. The model needs to be trained before this method is called.

All methods can be called with Dataframes or with an Anndata object. Either way the data has to be processed. We recommend to use Dataframes so you can choose the train test split yourself for more realistic results. If an Anndata object is provided, the train test split will be random and won't consider batches.
Additionally, you have to specify the batch id for each sample (e.g. the donor). The Conditional Autoencoder then learns to avoid batch effects.

```python
from clacell import CellClassifier

classifier = CellClassifier()

train_donor = adata_train.obs['Donor']
test_donor = adata_test.obs['Donor']

# 1. RandomSearch
print("\n1. random_search")
classifier.random_search(X_train, y_train, train_donor, X_test, y_test, test_donor, n_jobs=3)

# 2. Bayes Search
print("\n2. bayes_search")
classifier.bayes_search(X_train, y_train, train_donor, X_test, y_test, test_donor, n_jobs=3)

# 3. Train
print("\n3. train")
classifier.train(X_train, y_train, train_donor, C=0.001)

# 4. Evaluate
print("\n4. evaluate")
classifier.evaluate(X_test, y_test, log_to_console=True, log_to_file=True)

# 5. Predict
print("\n5. predict")
predictions = classifier.predict(X_test)
print(f"Macro F1: {f1_score(y_test, predictions, average="macro")}")
```


## Acknowledgments & Data Sources

The marker based annotation strategy is a reimplementation of the existing R package scumi-dev (licensed under BSD 3-Clause License). Link to the repository: https://bitbucket.org/jerry00/scumi-dev/src/master/
- **Citation:** Ding, J., Adiconis, X., Simmons, S.K. et al. Systematic comparison of single-cell and single-nucleus RNA-sequencing methods. Nat Biotechnol 38, 737–746 (2020). https://doi.org/10.1038/s41587-020-0465-8

This repository contains reference datasets used for training and validation:
- **CellTypist:** The Cross-tissue Immune Cell Atlas was provided by the **Teichmann Group at the Wellcome Sanger Institute** and were hosted by **Genome Research Limited** (licensed under CC BY-NC-ND 4.0). Link: https://www.tissueimmunecellatlas.org/
    - **Citation:**      C. Domínguez Conde et al., Cross-tissue immune cell analysis reveals tissue-specific features in humans. Science376, eabl5197(2022).DOI: [10.1126/science.abl5197](https://doi.org/10.1126/science.abl5197)
- **Human Cell Atlas (HCA):** HematopoieticImmuneCellAtlas (licensed under CC-BY 4.0). Project Link: https://explore.data.humancellatlas.org/projects/cc95ff89-2e68-4a08-a234-480eca21ce79
    - **Citation:** Li, B., Kowalczyk, M.S. et al. Hematopoietic Immune Cell Atlas. *Human Cell Atlas Data Portal* (2026).
