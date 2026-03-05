import pandas as pd
import matplotlib.pyplot as plt
def task_func(df, dct, columns=None, plot_histograms=False):
    """
    Replace values in a DataFrame with a dictionary mapping and optionally record histograms for specified columns.
    The function should raise the exception for:
        - The function will raise a ValueError is input df is not a DataFrame.
    The function should output with:
        - DataFrame: The DataFrame with replaced values. The columns are in the format of 'col1', 'col2', etc.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df must be a DataFrame")

    # Replace values in the DataFrame
    df = df.replace(dct)

    # Optionally record histograms for specified columns
    if plot_histograms:
        if columns is None:
            columns = df.columns
        for col in columns:
            plt.hist(df[col], bins=50)
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.title("Histogram of " + col)
            plt.show()

    return df
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10]})
dct = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}