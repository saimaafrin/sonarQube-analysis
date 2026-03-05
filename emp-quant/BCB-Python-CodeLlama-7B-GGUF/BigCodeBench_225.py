
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, dct, columns=None, plot_histograms=False):
    """
    Replace values in a DataFrame with a dictionary mapping and optionally record histograms for specified columns.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to be processed.
    dct : dict
        The dictionary mapping values to be replaced.
    columns : list, optional
        The columns to be processed. If None, all columns are processed.
    plot_histograms : bool, optional
        Whether to plot histograms for the replaced values.

    Returns
    -------
    df : pandas.DataFrame
        The processed DataFrame.

    Raises
    ------
    ValueError
        If input df is not a DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df must be a DataFrame.")

    # Replace values in the DataFrame
    df = df.replace(dct)

    # Optionally, plot histograms for the replaced values
    if plot_histograms:
        for col in columns:
            plt.hist(df[col], bins=50)
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.title("Histogram of {}".format(col))
            plt.show()

    return df