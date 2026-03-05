
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a non-empty DataFrame")
    if not df.select_dtypes(include=['number']).empty:
        raise ValueError("DataFrame must have at least one numeric column")
    fig, axs = plt.subplots(nrows=len(df.select_dtypes(include=['number']).columns), ncols=1, figsize=(10, 10))
    for i, col in enumerate(df.select_dtypes(include=['number']).columns):
        axs[i].hist(df[col], bins=50, label=col)
        axs[i].set_xlabel("Value")
        axs[i].set_ylabel("Frequency")
    return axs