import importlib
import sys
import pandas as pd
import resource
import time
import numpy as np


all_runs_data = []
num_runs = 10
start_run = 0
end_run = 9

for i in range(start_run, end_run + 1):
    print(f"=== Start Run {i+1}/{num_runs} ===")
    script_start = time.time()

    if 'train_conditional_autoencoder_rf_v3' in sys.modules:
        # Force python to rerun the script by reloading the module
        importlib.reload(train_conditional_autoencoder_rf_v3)
    else:
        # The first import executes the script
        import train_conditional_autoencoder_rf_v3
    
    total_script_time_min = (time.time() - script_start) / 60

    # Access the global variable of the training script
    df_run = train_conditional_autoencoder_rf_v3.robustness_results.copy()
    
    # Add Technical Metrics
    ## Runtime
    df_run[("All", "Technical_Metrics", "Resource_Usage", "Total_Pipeline_Time_Min")] = round(total_script_time_min, 2)

    ## Runtime per Iteration
    mean_fit_per_fold = train_conditional_autoencoder_rf_v3.tuned_classifier.cv_results_['mean_fit_time']
    mean_score_per_fold = train_conditional_autoencoder_rf_v3.tuned_classifier.cv_results_['mean_score_time']

    n_splits = 5

    total_time_per_iteration = (mean_fit_per_fold + mean_score_per_fold) * n_splits
    avg_time_per_iter_seconds = np.mean(total_time_per_iteration)
    dist = "All"
    cat = "Technical_Metrics"
    sub_cat = "Resource_Usage"
    metric = "Avg_Time_per_Iteration_Sec"
    df_run[(dist, cat, sub_cat, metric)] = round(avg_time_per_iter_seconds, 2)
    
    ## RAM Peak
    usage = resource.getrusage(resource.RUSAGE_SELF)
    peak_ram_gb = usage.ru_maxrss / (1024 * 1024)
    dist = "All"
    cat = "Technical_Metrics"
    sub_cat = "Resource_Usage"
    metric = "Peak_RAM_GB"
    df_run[(dist, cat, sub_cat, metric)] = peak_ram_gb
    
    ## Number of Epochs
    epochs = train_conditional_autoencoder_rf_v3.epoch + 1
    dist = "All"
    cat = "Technical_Metrics"
    sub_cat = "Training_Convergence"
    metric = "Autoencoder_Epochs"
    df_run[(dist, cat, sub_cat, metric)] = epochs

    df_run.to_csv(f'results/conditional_autoencoder_rf_higher_dropout/result_{i}.csv', index=True)
    all_runs_data.append(df_run)

current_count = len(all_runs_data)

# If there aren'T all Dataframes in the array, load them
if current_count < num_runs:
    loaded_samples = []
    needed_samples = num_samples - current_count
    print(
        f"There are {needed_samples} DataFrames missing. Load them from save directory..."
    )

    for i in range(needed_samples):
        file_path = f"results/conditional_autoencoder_rf_higher_dropout/result_{i}.csv"

        if os.path.exists(file_path):
            old_df = pd.read_csv(file_path, header=[0, 1, 2, 3], index_col=0)
            loaded_samples.append(old_df)
        else:
            print(
                f"Warning: File {file_path} not found! Skip it..."
            )
    all_runs_data = pd.concat([loaded_samples, all_runs_data], axis=0)

# Average over runs
combined_df = pd.concat(all_runs_data, axis=0)

# Compute Statistics for Robustness Test results
means = combined_df.mean()
stds = combined_df.std()

combined = means.round(4).astype(str) + " +- " + stds.round(4).astype(str)

# Create Dataframe with Statistics
stats_df = pd.DataFrame(
    [means, stds, combined], 
    index=["mean", "std", "mean +- std"], 
    columns=combined_df.columns
)

# Combine original Dataframe with Statistic Dataframe
final_df = pd.concat([combined_df, stats_df], axis=0)

print("=== Final result ===")
print(final_df.head())

final_df.to_csv('results/conditional_autoencoder_rf_higher_dropout/combined_result.csv', index=True)
