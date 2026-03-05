
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
TARGET_VALUES = np.array([1, 3, 4])
def task_func(df):
    # Replace all elements in DataFrame columns that do not exist in the TARGET_VALUES array with zeros
    df = df.replace(0, np.nan)
    df = df.fillna(0)
    # Perform Box-Cox transformation on each column
    for col in df.columns:
        data = df[col].values
        data = stats.boxcox(data, TARGET_VALUES)
        df[col] = data
    # Display KDE plots of the transformed columns
    fig, ax = plt.subplots(nrows=len(df.columns), ncols=1, figsize=(10, 10))
    for i, col in enumerate(df.columns):
        ax[i].hist(df[col].values, bins=50, alpha=0.5, label=col)
        ax[i].set_xlabel(col)
        ax[i].set_ylabel('Density')
    plt.show()
    return df