
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
TARGET_VALUES = np.array([1, 3, 4])

def task_func(df):
    # Replace elements not in TARGET_VALUES with zeros
    df = df.applymap(lambda x: x if x in TARGET_VALUES else 0)
    
    # Perform Box-Cox transformation
    transformed_df = df.apply(lambda x: stats.boxcox(x + 1)[0] if x.sum() != 0 else x)
    
    # Create KDE plots
    fig, axes = plt.subplots(nrows=1, ncols=len(transformed_df.columns), figsize=(12, 4))
    
    for i, column in enumerate(transformed_df.columns):
        axes[i].set_title(column)
        axes[i].set_xlabel('Value')
        axes[i].set_ylabel('Density')
        axes[i].plot(transformed_df[column], 'k.')
    
    plt.tight_layout()
    plt.show()
    
    return transformed_df, fig