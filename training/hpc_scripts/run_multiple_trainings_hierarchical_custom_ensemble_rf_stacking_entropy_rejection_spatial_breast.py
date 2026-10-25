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


# --- HIERARCHICAL CASCADE CLASSIFIER WITH UNCERTAINTY REJECTION ---
class HierarchicalCascadeClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, entropy_quantile=0.95):
        self.entropy_quantile = entropy_quantile
        self.coarse_classifier = None
        self.fine_classifiers = {}
        self.hierarchy_mapping = {}
        self.coarse_threshold = None
        self.fine_thresholds = {}

    def _get_subset(self, X, mask):
        if hasattr(X, "iloc"):
            return X.iloc[mask]
        return X[mask]

    def fit(self, X, y_coarse, y_fine, sorted_top_genes, coarse_rf_params):
        # 1. Coarse Custom Ensemble mit übergebenen Coarse-Hyperparametern bauen & trainieren
        print("  -> Trainiere Coarse Custom Stacking Ensemble...")
        self.coarse_classifier = build_custom_ensemble(sorted_top_genes, coarse_rf_params)
        self.coarse_classifier.fit(X, y_coarse)

        # Coarse Entropie-Schwelle für Rejection berechnen
        coarse_probs = self.coarse_classifier.predict_proba(X)
        coarse_entropies = -np.sum(coarse_probs * np.log2(coarse_probs + 1e-12), axis=1)
        self.coarse_threshold = np.quantile(coarse_entropies, self.entropy_quantile)
        print(f"  -> Coarse Rejection Entropy Threshold ({self.entropy_quantile*100}th percentile): {self.coarse_threshold:.4f}")

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
                print(f"Best CV Accuracy:  {opt.best_score_:.4f}")

                # Fine Ensemble trainieren
                print(f"  -> Trainiere Fine Custom Stacking Ensemble für '{coarse_label}'...")
                fine_ensemble = build_custom_ensemble(sorted_top_genes, best_rf_params)
                fine_ensemble.fit(X_subset, y_fine_subset)
                
                # Fine Entropie-Schwelle für Rejection berechnen
                fine_probs = fine_ensemble.predict_proba(X_subset)
                fine_entropies = -np.sum(fine_probs * np.log2(fine_probs + 1e-12), axis=1)
                fine_thresh = np.quantile(fine_entropies, self.entropy_quantile)
                self.fine_thresholds[coarse_label] = fine_thresh
                print(f"  -> Fine Rejection Entropy Threshold for '{coarse_label}': {fine_thresh:.4f}")

                self.fine_classifiers[coarse_label] = fine_ensemble
            else:
                print(f"  -> Überspringe '{coarse_label}' - hat keine echten Sub-Zelltypen (Leaf Node).")

        self.classes_ = np.unique(y_fine) 
        return self

    def predict_coarse(self, X):
        """Gibt Coarse Labels zurück und lehnt unsichere Zellen als 'Rejected' ab."""
        probs = self.coarse_classifier.predict_proba(X)
        preds = self.coarse_classifier.classes_[np.argmax(probs, axis=1)]
        entropies = -np.sum(probs * np.log2(probs + 1e-12), axis=1)
        
        if self.coarse_threshold is not None:
            rejected = entropies > self.coarse_threshold
            preds = preds.astype(object)
            preds[rejected] = "Rejected"
        return preds

    def predict_fine(self, X, coarse_preds=None):
        """Gibt Fine Labels zurück und übernimmt Rejections."""
        if coarse_preds is None:
            coarse_preds = self.predict_coarse(X)
            
        fine_preds = np.empty_like(coarse_preds, dtype=object)
        
        # Bereits auf Coarse-Ebene abgelehnte Zellen bleiben Rejected
        already_rejected = (coarse_preds == "Rejected")
        fine_preds[already_rejected] = "Rejected"
        
        unique_predicted_coarse = np.unique(coarse_preds[~already_rejected])
        
        for coarse_label in unique_predicted_coarse:
            mask = (coarse_preds == coarse_label)
            if not np.any(mask):
                continue
                
            X_subset = self._get_subset(X, mask)
            
            if coarse_label in self.fine_classifiers:
                fine_ensemble = self.fine_classifiers[coarse_label]
                probs = fine_ensemble.predict_proba(X_subset)
                sub_preds = fine_ensemble.classes_[np.argmax(probs, axis=1)]
                entropies = -np.sum(probs * np.log2(probs + 1e-12), axis=1)
                
                if coarse_label in self.fine_thresholds:
                    rejected = entropies > self.fine_thresholds[coarse_label]
                    sub_preds = sub_preds.astype(object)
                    sub_preds[rejected] = "Rejected"
                fine_preds[mask] = sub_preds
            else:
                fine_preds[mask] = self.hierarchy_mapping.get(coarse_label, [coarse_label])[0]
                
        return fine_preds

    def predict(self, X):
        """Gibt ein Tuple (coarse_preds, fine_preds) zurück."""
        coarse_preds = self.predict_coarse(X)
        fine_preds = self.predict_fine(X, coarse_preds=coarse_preds)
        return coarse_preds, fine_preds


# --- DATA LOADING & PREPROCESSING ---
adata = ad.read_h5ad('/home/woody/iwbn/iwbn133h/data/10x-gex/breast/0fbf6fa3-8463-46ab-bda8-9703848b58db_spatial_fine_and_coarse_annotated.h5ad')

# Use raw counts
#adata = adata.raw.to_adata()
# Check if counts are raw data
if hasattr(adata.X, "sum"):
    per_cell_totals = np.asarray(adata.X.sum(axis=1)).ravel()
else:
    per_cell_totals = np.sum(adata.X, axis=1)

print("min:", np.min(per_cell_totals))
print("median:", np.median(per_cell_totals))
print("mean:", np.mean(per_cell_totals))
print("max:", np.max(per_cell_totals))

# Preprocessing
adata = prepare_adata(adata, batch_key="donor_id")

# Create train test split
donor_train = [
    'pal_Patient 0177', 'wu_natgen_CID4471', 'TBB129', 'BC392_Tumor',
]
donor_test = [
    'pal_Patient 0176', 'TBB338', 'wu_natgen_CID44971', 'BC393_Tumor',
]

adata_train = adata[adata.obs["donor_id"].isin(donor_train)].copy()
adata_test = adata[adata.obs["donor_id"].isin(donor_test)].copy()

# Prepare Data for training 
X_train = adata_train.to_df()
y_train_coarse = adata_train.obs['scumi_clean_coarse'].values
y_train_fine = adata_train.obs['scumi_clean_fine_grained'].values

X_test = adata_test.to_df()
y_test_coarse = adata_test.obs['scumi_clean_coarse'].values
y_test_fine = adata_test.obs['scumi_clean_fine_grained'].values

# Print the first 5 cells to show the gene names
print(X_train[:5])

all_runs_data_coarse = []
all_runs_data_fine = []

num_runs = 10
start_run = 0
end_run = 9

base_dir = 'results/hierarchical_custom_ensemble_rf_stacking_entropy_rejection_spatial_breast'
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

    # Compute optimal hyperparameters for the coarse classifier using BayesSearchCV
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
    opt.fit(X_train, y_train_coarse, callback=my_stopper)
    
    hyperparameters = opt.best_params_
    print(f"\nSearch terminated after {len(opt.cv_results_['mean_test_score'])} Iterations.")
    print(f"Test-Split Accuracy:  {opt.score(X_test, y_test_coarse):.4f}")
    
    # Hierarchical classifier mit Entropie-Rejection (quantil 0.95) initialisieren
    best_model = HierarchicalCascadeClassifier(entropy_quantile=0.95)
    best_model.fit(
        X=X_train, 
        y_coarse=y_train_coarse, 
        y_fine=y_train_fine, 
        sorted_top_genes=sorted_top_genes, 
        coarse_rf_params=hyperparameters
    )
    
    training_time_min = (time.time() - train_start) / 60
    print(f"\nGesamte Trainingszeit für Run {i+1}: {training_time_min:.2f} Minuten")

    y_pred_coarse, y_pred_fine = best_model.predict(X_test)
    
    # Rejection-Statistik ausgeben
    coarse_rejection_rate = np.mean(y_pred_coarse == "Rejected") * 100
    fine_rejection_rate = np.mean(y_pred_fine == "Rejected") * 100
    print(f"\n[REJECTION STATS] Coarse Rejected: {coarse_rejection_rate:.2f}% | Fine Rejected: {fine_rejection_rate:.2f}%")

    print("\n--- EVALUATION AUF DEN TESTDATEN ---")
    print(f"[COARSE] Test Accuracy: {accuracy_score(y_test_coarse, y_pred_coarse):.4f} | Macro F1: {f1_score(y_test_coarse, y_pred_coarse, average='macro'):.4f}")
    print(f"[FINE]   Test Accuracy: {accuracy_score(y_test_fine, y_pred_fine):.4f} | Macro F1: {f1_score(y_test_fine, y_pred_fine, average='macro'):.4f}")

    with open("pegasus_feature_importance_interleaved_marker_genes.pkl", "rb") as f:
        feature_importance = pickle.load(f)

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
        CoarseWrapper(best_model), X_test, y_test_coarse, adata_test.obs['donor_id'],
        'scumi_clean_coarse', None, feature_importance,
        log_to_console=True, log_to_file=False,
    )
    coarse_eval_time_min = (time.time() - eval_start_coarse) / 60
    coarse_total_time_min = training_time_min + coarse_eval_time_min

    # --- 3. EVALUIERUNG & ZEITMESSUNG: FINE-GRAINED ---
    print("Führe Robustness-Test für FINE-GRAINED Labels durch...")
    eval_start_fine = time.time()
    robustness_fine = test_robustness(
        FineWrapper(best_model), X_test, y_test_fine, adata_test.obs['donor_id'],
        'scumi_clean_fine_grained', None, feature_importance,
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
