import importlib
import sys
import pandas as pd
import resource
import time
import numpy as np
import pickle
import os

from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import StackingClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, f1_score

import anndata as ad
import scanpy as sc
import joblib

# BayesSearch und CustomStopper exakt wie im Vorlage-Skript
from skopt import BayesSearchCV
from skopt.space import Categorical, Integer
from custom_stopper import CustomStopper

from test_robustness_higher_dropout import test_robustness
from preprocess_data import prepare_adata


# --- HELPER FUNKTION FÜR DEN CUSTOM STACKING ENSEMBLE BUILD ---
def build_custom_ensemble(sorted_top_genes, rf_params):
    total_genes = len(sorted_top_genes)

    drop_075_pct = int(total_genes * 0.0075)
    drop_15_pct = int(total_genes * 0.015)
    drop_25_pct = int(total_genes * 0.025)

    features_model_all = sorted_top_genes
    features_model_minus_075 = sorted_top_genes[drop_075_pct:]
    features_model_minus_15 = sorted_top_genes[drop_15_pct:]
    features_model_minus_25 = sorted_top_genes[drop_25_pct:]

    def make_pipeline(features_to_keep, model_name):
        preprocessor = ColumnTransformer(
            transformers=[('keep', 'passthrough', features_to_keep)],
            remainder='drop'
        )
        # Alle RFs erhalten dieselben Hyperparameter
        model = RandomForestClassifier(class_weight='balanced', **rf_params)
        return Pipeline([
            ('select', preprocessor),
            (model_name, model)
        ])

    ensemble = StackingClassifier(
        estimators=[
            ('all_features', make_pipeline(features_model_all, 'rf_all')),
            ('minus_075_pct', make_pipeline(features_model_minus_075, 'rf_075')),
            ('minus_15_pct', make_pipeline(features_model_minus_15, 'rf_15')),
            ('minus_25_pct', make_pipeline(features_model_minus_25, 'rf_25'))
        ],
        final_estimator=LogisticRegression(max_iter=1000),
        cv=5,
        n_jobs=-1,
        passthrough=False
    )
    return ensemble


# --- HIERARCHICAL CASCADE CLASSIFIER ---
class HierarchicalCascadeClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self):
        self.coarse_classifier = None
        self.fine_classifiers = {}
        self.hierarchy_mapping = {}

    def _get_subset(self, X, mask):
        if hasattr(X, "iloc"):
            return X.iloc[mask]
        return X[mask]

    def fit(self, X, y_coarse, y_fine, sorted_top_genes, coarse_rf_params):
        # 1. Coarse Custom Ensemble mit übergebenen Coarse-Hyperparametern bauen & trainieren
        print("  -> Trainiere Coarse Custom Stacking Ensemble...")
        self.coarse_classifier = build_custom_ensemble(sorted_top_genes, coarse_rf_params)
        self.coarse_classifier.fit(X, y_coarse)

        # 2. Fine-Grained Classifiers je Coarse Label bauen & trainieren
        unique_coarse_labels = np.unique(y_coarse)
        
        for coarse_label in unique_coarse_labels:
            mask = (y_coarse == coarse_label)
            X_subset = self._get_subset(X, mask)
            y_fine_subset = y_fine[mask]
            
            unique_fine = np.unique(y_fine_subset)
            self.hierarchy_mapping[coarse_label] = unique_fine
            
            if len(unique_fine) > 1:
                print(f"\n  -> Starte BayesSearch für Fine-Grained Label '{coarse_label}' ({len(unique_fine)} Sub-Zelltypen)...")
                
                # Exakte BayesSearch-Konfiguration laut train_randomforest_bayes.py
                model = RandomForestClassifier(class_weight='balanced')
                search_space = {
                    'n_estimators': Integer(100, 250, prior='log-uniform'),
                    'max_depth': Integer(10, 30),
                    'max_features': Categorical(['sqrt', 'log2'])
                }
                my_stopper = CustomStopper(patience=5, min_delta=0.002, min_iter=15)

                opt = BayesSearchCV(
                    estimator=model,
                    search_spaces=search_space,
                    n_iter=30,
                    cv=5,
                    scoring='accuracy',
                    n_jobs=-1,
                    verbose=10
                )
                print("Start BayesSearch with Early Stopping...")
                opt.fit(X_subset, y_fine_subset, callback=my_stopper)
                
                best_rf_params = opt.best_params_
                print(f"\nSearch terminated after {len(opt.cv_results_['mean_test_score'])} Iterations.")
                print(f"Best hyperparameters for '{coarse_label}': {opt.best_params_}")
                print(f"Test-Split Accuracy:  {opt.score(X_test, y_fine_subset):.4f}")

                # Das Custom Ensemble mit den optimierten RF-Hyperparametern bauen und auf dem Subset trainieren
                print(f"  -> Trainiere Fine Custom Stacking Ensemble für '{coarse_label}'...")
                fine_ensemble = build_custom_ensemble(sorted_top_genes, best_rf_params)
                fine_ensemble.fit(X_subset, y_fine_subset)
                
                self.fine_classifiers[coarse_label] = fine_ensemble
            else:
                print(f"  -> Überspringe '{coarse_label}' - hat keine echten Sub-Zelltypen (Leaf Node).")

        self.classes_ = np.unique(y_fine) 
        return self

    def predict_coarse(self, X):
        """Gibt nur die Coarse Labels zurück."""
        return self.coarse_classifier.predict(X)

    def predict_fine(self, X, coarse_preds=None):
        """Gibt nur die Fine Labels zurück. Optional können bereits berechnete Coarse Labels übergeben werden."""
        if coarse_preds is None:
            coarse_preds = self.predict_coarse(X)
            
        fine_preds = np.empty_like(coarse_preds, dtype=object)
        unique_predicted_coarse = np.unique(coarse_preds)
        
        for coarse_label in unique_predicted_coarse:
            mask = (coarse_preds == coarse_label)
            
            if coarse_label in self.fine_classifiers:
                X_subset = self._get_subset(X, mask)
                fine_preds[mask] = self.fine_classifiers[coarse_label].predict(X_subset)
            else:
                fine_preds[mask] = self.hierarchy_mapping.get(coarse_label, [coarse_label])[0]
                
        return fine_preds

    def predict(self, X):
        """Gibt ein Tuple (coarse_preds, fine_preds) zurück."""
        coarse_preds = self.predict_coarse(X)
        fine_preds = self.predict_fine(X, coarse_preds=coarse_preds)
        return coarse_preds, fine_preds


# --- DATA LOADING & PREPROCESSING ---
adata = ad.read_h5ad('/home/woody/iwbn/iwbn133h/data/CellTypist_HumanCellAtlas_Merged_cleaned_refined_cell_types_fine_and_coarse.h5ad')

# Use raw data instead of already preprocessed data
adata.X = adata.layers['counts'].copy()

# Preprocessing
adata = prepare_adata(adata, batch_key="Donor")

# Create train test split
donor_train = ['637C', 'A35', 'A36', 'D503', '2', '3', '4', '6']
donor_test = ['621B', 'D496', '7', '8']

adata_train = adata[adata.obs["Donor"].isin(donor_train)].copy()
adata_test = adata[adata.obs["Donor"].isin(donor_test)].copy()

# Prepare Data for training 
X_train = adata_train.to_df()
y_train_coarse = adata_train.obs['scumi_clean_coarse'].values
y_train_fine = adata_train.obs['scumi_clean_fine_grained'].values

X_test = adata_test.to_df()
y_test_coarse = adata_test.obs['scumi_clean_coarse'].values
y_test_fine = adata_test.obs['scumi_clean_fine_grained'].values

# Coarse Labels Hyperparameters
hyperparameters = {
        0: {'max_depth': 29, 'max_features': 'sqrt', 'n_estimators': 242},
        1: {'max_depth': 30, 'max_features': 'sqrt', 'n_estimators': 248},
        2: {'max_depth': 30, 'max_features': 'sqrt', 'n_estimators': 100},
        3: {'max_depth': 30, 'max_features': 'sqrt', 'n_estimators': 249},
        4: {'max_depth': 29, 'max_features': 'sqrt', 'n_estimators': 250},
        5: {'max_depth': 30, 'max_features': 'sqrt', 'n_estimators': 246},
        6: {'max_depth': 30, 'max_features': 'sqrt', 'n_estimators': 250},
        7: {'max_depth': 30, 'max_features': 'sqrt', 'n_estimators': 250},
        8: {'max_depth': 30, 'max_features': 'sqrt', 'n_estimators': 245},
        9: {'max_depth': 28, 'max_features': 'sqrt', 'n_estimators': 219},
}

all_runs_data_coarse = []
all_runs_data_fine = []

num_runs = 10
start_run = 0
end_run = 9

base_dir = 'results/hierarchical_custom_ensemble_rf_stacking'
coarse_dir = base_dir + '_coarse'
fine_dir = base_dir + '_fine_grained'

for i in range(start_run, end_run + 1):
    print(f"\n==================== Start Run {i+1}/{num_runs} ====================")

    # Feature Importance Bestimmung via LinearSVC auf Fine-Grained Ebene
    rf = LinearSVC()
    rf.fit(X_train, y_train_fine)
    importance = np.mean(np.abs(rf.coef_), axis=0)

    sorted_indices = np.argsort(importance)[::-1]
    sorted_top_genes = X_train.columns[sorted_indices].tolist()

    # --- 1. MODELL-TRAINING UND MESSUNG DER TRAININGSZEIT ---
    train_start = time.time()
    
    best_model = HierarchicalCascadeClassifier()
    best_model.fit(
        X=X_train, 
        y_coarse=y_train_coarse, 
        y_fine=y_train_fine, 
        sorted_top_genes=sorted_top_genes, 
        coarse_rf_params=hyperparameters[i]
    )
    
    training_time_min = (time.time() - train_start) / 60
    print(f"\nGesamte Trainingszeit für Run {i+1}: {training_time_min:.2f} Minuten")

    y_pred_coarse, y_pred_fine = best_model.predict(X_test)
    
    print("\n--- EVALUATION AUF DEN TESTDATEN ---")
    print(f"[COARSE] Test Accuracy: {accuracy_score(y_test_coarse, y_pred_coarse):.4f} | Macro F1: {f1_score(y_test_coarse, y_pred_coarse, average='macro'):.4f}")
    print(f"[FINE]   Test Accuracy: {accuracy_score(y_test_fine, y_pred_fine):.4f} | Macro F1: {f1_score(y_test_fine, y_pred_fine, average='macro'):.4f}")

    with open("pegasus_feature_importance_interleaved_marker_genes.pkl", "rb") as f:
        feature_importance = pickle.load(f)

    ood_datasets = {
        'HIHA_Pediatric': '/home/woody/iwbn/iwbn133h/data/human_immune_health_atlas/human_immune_health_atlas_sampled_Children_10k.h5ad',
        'HIHA_Young_Adult': '/home/woody/iwbn/iwbn133h/data/human_immune_health_atlas/human_immune_health_atlas_sampled_Young_Adult_10k.h5ad',
        'HIHA_Older_Adult': '/home/woody/iwbn/iwbn133h/data/human_immune_health_atlas/human_immune_health_atlas_sampled_Older_Adult_10k.h5ad',
        'AIDA': '/home/woody/iwbn/iwbn133h/data/AIDA/aida_sampled_10k.h5ad',
    }
    
    class CoarseWrapper:
        def __init__(self, model): self.model = model
        def predict(self, X): return self.model.predict_coarse(X)
        
    class FineWrapper:
        def __init__(self, model): self.model = model
        def predict(self, X): return self.model.predict_fine(X)

    # --- 2. EVALUIERUNG & ZEITMESSUNG: COARSE ---
    print("\nFühre Robustness-Test für COARSE Labels durch...")
    eval_start_coarse = time.time()
    robustness_coarse = test_robustness(
        CoarseWrapper(best_model), X_test, y_test_coarse, adata_test.obs['Donor'],
        'scumi_clean_coarse', ood_datasets, feature_importance,
        log_to_console=True, log_to_file=False,
    )
    coarse_eval_time_min = (time.time() - eval_start_coarse) / 60
    coarse_total_time_min = training_time_min + coarse_eval_time_min

    # --- 3. EVALUIERUNG & ZEITMESSUNG: FINE-GRAINED ---
    print("Führe Robustness-Test für FINE-GRAINED Labels durch...")
    eval_start_fine = time.time()
    robustness_fine = test_robustness(
        FineWrapper(best_model), X_test, y_test_fine, adata_test.obs['Donor'],
        'scumi_clean_fine_grained', ood_datasets, feature_importance,
        log_to_console=True, log_to_file=False,
    )
    fine_eval_time_min = (time.time() - eval_start_fine) / 60
    fine_total_time_min = training_time_min + fine_eval_time_min

    # Peak RAM Bestimmung
    usage = resource.getrusage(resource.RUSAGE_SELF)
    peak_ram_gb = usage.ru_maxrss / (1024 * 1024)

    # --- 4. ZUWEISUNG DER ZEITEN UND SPEICHERN ---
    # Coarse Dataframe Metriken
    df_run_coarse = robustness_coarse.copy()
    df_run_coarse[("All", "Technical_Metrics", "Resource_Usage", "Training_Time_Min")] = round(training_time_min, 2)
    df_run_coarse[("All", "Technical_Metrics", "Resource_Usage", "Inference_Evaluation_Time_Min")] = round(coarse_eval_time_min, 2)
    df_run_coarse[("All", "Technical_Metrics", "Resource_Usage", "Total_Pipeline_Time_Min")] = round(coarse_total_time_min, 2)
    df_run_coarse[("All", "Technical_Metrics", "Resource_Usage", "Peak_RAM_GB")] = peak_ram_gb

    # Fine-Grained Dataframe Metriken
    df_run_fine = robustness_fine.copy()
    df_run_fine[("All", "Technical_Metrics", "Resource_Usage", "Training_Time_Min")] = round(training_time_min, 2)
    df_run_fine[("All", "Technical_Metrics", "Resource_Usage", "Inference_Evaluation_Time_Min")] = round(fine_eval_time_min, 2)
    df_run_fine[("All", "Technical_Metrics", "Resource_Usage", "Total_Pipeline_Time_Min")] = round(fine_total_time_min, 2)
    df_run_fine[("All", "Technical_Metrics", "Resource_Usage", "Peak_RAM_GB")] = peak_ram_gb

    df_run_coarse.to_csv(os.path.join(coarse_dir, f'result_{i}.csv'), index=True)
    df_run_fine.to_csv(os.path.join(fine_dir, f'result_{i}.csv'), index=True)
    
    all_runs_data_coarse.append(df_run_coarse)
    all_runs_data_fine.append(df_run_fine)


# --- AGGREGATION FUNKTION ---
def aggregate_and_save(data_list, folder_path, level_name):
    current_count = len(data_list)
    
    if current_count < num_runs:
        loaded_samples = []
        needed_samples = num_runs - current_count
        print(f"Lade {needed_samples} fehlende DataFrames für {level_name} aus {folder_path}...")

        for i in range(needed_samples):
            file_path = os.path.join(folder_path, f"result_{i}.csv")
            if os.path.exists(file_path):
                old_df = pd.read_csv(file_path, header=[0, 1, 2, 3], index_col=0)
                loaded_samples.append(old_df)
            else:
                print(f"Warning: File {file_path} not found! Skip it...")
        data_list = loaded_samples + data_list

    combined_df = pd.concat(data_list, axis=0)
    means = combined_df.mean()
    stds = combined_df.std()
    combined = means.round(4).astype(str) + " +- " + stds.round(4).astype(str)

    stats_df = pd.DataFrame(
        [means, stds, combined], 
        index=["mean", "std", "mean +- std"], 
        columns=combined_df.columns
    )

    final_df = pd.concat([combined_df, stats_df], axis=0)
    final_df.to_csv(os.path.join(folder_path, 'combined_result.csv'), index=True)
    return final_df

print("\n=== Finalisiere COARSE Ergebnisse ===")
final_coarse = aggregate_and_save(all_runs_data_coarse, coarse_dir, "COARSE")

print("\n=== Finalisiere FINE-GRAINED Ergebnisse ===")
final_fine = aggregate_and_save(all_runs_data_fine, fine_dir, "FINE-GRAINED")