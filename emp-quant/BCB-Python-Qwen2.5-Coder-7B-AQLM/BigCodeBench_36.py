
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

TARGET_VALUES = np.array([1, 3, 4])

def task_func(df):
    # Replace values not in TARGET_VALUES with 0
    for col in df.columns:
        df[col] = df[col].apply(lambda x: x if x in TARGET_VALUES else 0)
    
    # Perform Box-Cox transformation
    transformed_df = df.copy()
    for col in df.columns:
        if df[col].nunique() > 1:  # Check if column is not constant
            transformed_df[col] = stats.boxcox(df[col] + 1)[0]
    
    # Plot KDE plots
    fig, axes = plt.subplots(nrows=len(transformed_df.columns), ncols=1, figsize=(8, 6 * len(transformed_df.columns)))
    for ax, col in zip(axes, transformed_df.columns):
        ax.set_title(f'KDE Plot of {col}')
        ax.set_xlabel(col)
        ax.set_ylabel('Density')
        stats.kdeplot(transformed_df[col], ax=ax)
    
    plt.tight_layout()
    plt.show()
    
    return transformed_df, fig