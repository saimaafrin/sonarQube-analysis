
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, dct, columns=None, plot_histograms=False):
    """
    Replace values in a DataFrame with a dictionary mapping and optionally record histograms for specified columns.
    The function will raise a ValueError if input df is not a DataFrame.
    The function will output with:
        DataFrame: The DataFrame with replaced values. The columns are in the format of 'col1', 'col2', etc.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df must be a DataFrame")
    if columns is None:
        columns = df.columns
    if plot_histograms:
        for col in columns:
            plt.hist(df[col], bins=50)
            plt.xlabel(col)
            plt.ylabel("Count")
            plt.show()
    for col in columns:
        if col in dct:
            df[col] = dct[col]
    return df