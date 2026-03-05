
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

TARGET_VALUES = np.array([1, 3, 4])

def task_func(df):
    # Replace all elements in DataFrame columns that do not exist in the TARGET_VALUES array with zeros
    df = df.replace(to_replace=np.setdiff1d(df.columns, TARGET_VALUES), value=0)

    # Perform a Box-Cox transformation on each column (if data is not constant, add 1 to account for zeros)
    for col in df.columns:
        if not np.all(df[col] == 0):
            df[col] = np.power(df[col] + 1, 1/0.5)

    # Display the resulting KDE plots
    fig, axs = plt.subplots(ncols=len(df.columns), figsize=(10, 6))
    for i, col in enumerate(df.columns):
        sns.kdeplot(df[col], ax=axs[i])
        axs[i].set_title(col)
    plt.tight_layout()

    return df, fig