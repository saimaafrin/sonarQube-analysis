
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

TARGET_VALUES = np.array([1, 3, 4])

def task_func(df):
    # Replace values not in TARGET_VALUES with zero
    df_transformed = df.applymap(lambda x: x if x in TARGET_VALUES else 0)
    
    # Perform Box-Cox transformation
    fig, axes = plt.subplots(len(df_transformed.columns), figsize=(10, len(df_transformed.columns)*2))
    for i, col in enumerate(df_transformed.columns):
        if df_transformed[col].nunique() > 1:  # Check if column has more than one unique value
            df_transformed[col] += 1  # Add 1 to avoid log(0)
            df_transformed[col], _ = stats.boxcox(df_transformed[col])
            df_transformed[col] -= 1  # Subtract 1 to revert back to original scale
            df_transformed[col].plot(kind='kde', ax=axes[i])
            axes[i].set_title(f'KDE Plot of {col}')
        else:
            axes[i].text(0.5, 0.5, 'Constant Data', horizontalalignment='center', verticalalignment='center')
            axes[i].axis('off')
    
    plt.tight_layout()
    return df_transformed, fig