
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

TARGET_VALUES = np.array([1, 3, 4])

def task_func(df):
    # Replace elements not in TARGET_VALUES with zeros
    for column in df.columns:
        df[column] = np.where(np.isin(df[column], TARGET_VALUES), df[column], 0)
    
    # Perform Box-Cox transformation
    transformed_df = df.copy()
    for column in df.columns:
        if df[column].std() != 0:
            transformed_df[column], _ = stats.boxcox(df[column] + 1)
        else:
            transformed_df[column] = 0
    
    # Plot KDE plots
    fig, axes = plt.subplots(nrows=1, ncols=len(df.columns), figsize=(15, 3))
    for i, column in enumerate(df.columns):
        axes[i].kdeplot(transformed_df[column], shade=True)
        axes[i].set_title(f'KDE Plot of {column}')
    
    plt.tight_layout()
    plt.show()
    
    return transformed_df, fig