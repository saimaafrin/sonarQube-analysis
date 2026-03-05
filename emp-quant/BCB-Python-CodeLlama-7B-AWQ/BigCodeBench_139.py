import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(df):
    """
    Draw histograms of numeric columns in a DataFrame and return the plots.
    Each histogram represents the distribution of values in one numeric column,
    with the column name as the plot title, 'Value' as the x-axis label, and
    'Frequency' as the y-axis label.
    """
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame with numeric columns.")

    numeric_columns = df.select_dtypes(include=np.number).columns
    if not numeric_columns:
        raise ValueError("DataFrame has no numeric columns.")

    fig, axs = plt.subplots(nrows=len(numeric_columns), ncols=1, figsize=(10, 10))
    for i, col in enumerate(numeric_columns):
        axs[i].hist(df[col], bins=50, label=col)
        axs[i].set_title(col)
        axs[i].set_xlabel("Value")
        axs[i].set_ylabel("Frequency")

    return axs
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [1, 2, 3, 4, 5], "C": [1, 2, 3, 4, 5]})