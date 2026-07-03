import importlib
import sys
import pandas as pd
import resource
import time
import numpy as np


all_runs_data = []
num_runs = 10

for i in range(num_runs):
    print(f"=== Start Run {i+1}/{num_runs} ===")
    script_start = time.time()

    if 'train_randomforest_bayes' in sys.modules:
        # Force python to rerun the script by reloading the module
        importlib.reload(train_randomforest_bayes)
    else:
        # The first import executes the script
        import train_randomforest_bayes
    
    total_script_time_min = (time.time() - script_start) / 60

    # Access the global variable of the training script
    df_run = train_randomforest_bayes.robustness_results.copy()
    
    # Add Technical Metrics
    ## Runtime
    df_run.loc[("All", "Technical_Metrics", "Resource_Usage", "Total_Pipeline_Time_Min"), "Value"] = round(total_script_time_min, 2)

    ## Runtime per Iteration
    mean_fit_per_fold = opt.cv_results_['mean_fit_time']
    mean_score_per_fold = opt.cv_results_['mean_score_time']

    n_splits = 5

    total_time_per_iteration = (mean_fit_per_fold + mean_score_per_fold) * n_splits
    avg_time_per_iter_seconds = np.mean(total_time_per_iteration)
    dist = "All"
    cat = "Technical_Metrics"
    sub_cat = "Resource_Usage"
    metric = "Avg_Time_per_Iteration_Sec"
    df_run.loc[(dist, cat, sub_cat, metric), "Value"] = round(avg_time_per_iter_seconds, 2)
    
    ## RAM Peak
    usage = resource.getrusage(resource.RUSAGE_SELF)
    peak_ram_gb = usage.ru_maxrss / (1024 * 1024)
    dist = "All"
    cat = "Technical_Metrics"
    sub_cat = "Resource_Usage"
    metric = "Peak_RAM_GB"
    df_run.loc[(dist, cat, sub_cat, metric), "Value"] = peak_ram_gb

    df_run.to_csv(f'results/randomforest/result_{i}.csv', index=True)
    all_runs_data.append(df_run)


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

final_df.to_csv('results/randomforest/combined_result.csv', index=True)
