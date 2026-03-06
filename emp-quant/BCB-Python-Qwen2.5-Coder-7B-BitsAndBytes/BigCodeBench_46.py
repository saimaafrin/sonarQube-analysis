
from scipy.stats import zscore
import matplotlib.pyplot as plt

def task_func(df):
    # Replace missing values with the mean of the respective column
    df_filled = df.fillna(df.mean())
    
    # Calculate Z-scores for numeric columns
    z_scores_df = df_filled.apply(zscore)
    
    # Create a list to hold the Axes objects for histograms
    axes_list = []
    
    # Plot histograms for each numeric column
    fig, axes = plt.subplots(len(df.columns), 1, figsize=(8, len(df.columns)*4))
    if len(df.columns) == 1:
        axes = [axes]  # Ensure axes is a list even if there's only one column
    
    for i, col in enumerate(df.columns):
        axes[i].hist(df_filled[col], bins=10, edgecolor='black')
        axes[i].set_title(f'Histogram of {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Frequency')
        axes_list.append(axes[i])
    
    plt.tight_layout()
    plt.show()
    
    return z_scores_df, axes_list