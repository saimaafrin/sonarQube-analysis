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
        raise ValueError("Input df is not a DataFrame.")

    # Replace values in the DataFrame with the dictionary mapping
    df = df.replace(dct)

    # Optionally record histograms for specified columns
    if columns is not None and plot_histograms:
        for col in columns:
            plt.hist(df[col], bins=20)
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.title(f"Histogram of {col}")
            plt.show()

    return df
df = pd.DataFrame({"col1": [1, 2, 3, 4, 5], "col2": [6, 7, 8, 9, 10]})
dct = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}