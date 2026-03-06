
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

TARGET_VALUES = np.array([1, 3, 4])

def task_func(df):
    # Replace all elements in DataFrame columns that do not exist in the TARGET_VALUES array with zeros
    df = df.fillna(0)

    # Perform Box-Cox transformation on each column (if data is not constant, add 1 to account for zeros)
    for col in df.columns:
        if df[col].var() > 0:
            df[col] = np.log(df[col] + 1)

    # Display KDE plots of the transformed columns
    fig, axs = plt.subplots(ncols=len(df.columns), figsize=(12, 6))
    for i, col in enumerate(df.columns):
        sns.kdeplot(df[col], ax=axs[i])
        axs[i].set_title(f"KDE Plot of {col}")

    return df, fig