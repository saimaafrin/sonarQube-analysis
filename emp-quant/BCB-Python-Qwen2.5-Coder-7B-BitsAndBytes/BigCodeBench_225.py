
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, dct, columns=None, plot_histograms=False):
    """
    Replace values in a DataFrame with a dictionary mapping and optionally record histograms for specified columns.

    Parameters:
    - df (pd.DataFrame): Input DataFrame to be modified.
    - dct (dict): Dictionary mapping old values to new values.
    - columns (list, optional): List of column names to plot histograms for after replacement. Defaults to None.
    - plot_histograms (bool, optional): Whether to plot histograms for specified columns. Defaults to False.

    Returns:
    - pd.DataFrame: DataFrame with replaced values.
    """
    
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    # Replace values in the DataFrame using the provided dictionary
    df_replaced = df.replace(dct)
    
    # Optionally plot histograms for specified columns
    if plot_histograms and columns:
        for col in columns:
            if col in df_replaced.columns:
                df_replaced[col].hist()
                plt.title(f'Histogram of {col}')
                plt.xlabel(col)
                plt.ylabel('Frequency')
                plt.show()
            else:
                print(f"Column '{col}' not found in DataFrame.")
    
    return df_replaced