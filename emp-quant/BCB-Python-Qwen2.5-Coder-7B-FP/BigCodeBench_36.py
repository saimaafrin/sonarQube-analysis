import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
TARGET_VALUES = np.array([1, 3, 4])
def task_func(df):
    # Replace values not in TARGET_VALUES with 0
    for col in df.columns:
        df[col] = np.where(np.isin(df[col], TARGET_VALUES), df[col], 0)
    
    # Perform Box-Cox transformation
    transformed_df = df.copy()
    for col in df.columns:
        if df[col].nunique() > 1:  # Check if column is not constant
            transformed_df[col] = df[col] + 1  # Add 1 to account for zeros
            transformed_df[col], _ = stats.boxcox(transformed_df[col])
    
    # Plot KDE plots
    fig, axes = plt.subplots(nrows=1, ncols=len(transformed_df.columns), figsize=(15, 3))
    for ax, col in zip(axes, transformed_df.columns):
        transformed_df[col].plot(kind='kde', ax=ax)
        ax.set_title(f'KDE Plot of {col}')
    
    plt.tight_layout()
    plt.show()
    
    return transformed_df, fig