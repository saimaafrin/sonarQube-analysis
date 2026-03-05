import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(data, column="c"):
    """
    Remove a column from a data dictionary if it exists, and then plot the remaining data if it contains numeric data.
    The function should output with:
        df (pd.DataFrame): The modified DataFrame after removing the specified column.
        ax (matplotlib.axes._axes.Axes or None): The plot of the modified DataFrame if there's
        numeric data to plot, otherwise None.
    """
    # Check if the column exists in the DataFrame
    if column in data.columns:
        # Remove the column from the DataFrame
        df = data.drop(columns=[column])
    else:
        # Raise an error if the column does not exist
        raise ValueError(f"Column {column} does not exist in the DataFrame")

    # Check if the DataFrame contains any numeric data
    if df.select_dtypes(include=np.number).shape[1] > 0:
        # Plot the DataFrame
        ax = df.plot(kind="line", x="index", y=df.columns)
    else:
        # Raise an error if the DataFrame does not contain any numeric data
        raise ValueError("DataFrame does not contain any numeric data")

    return df, ax
data = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})