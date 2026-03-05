import pandas as pd
import matplotlib.pyplot as plt
def task_func(df, dct, columns=None, plot_histograms=False):
    """
    Replace values in a DataFrame with a dictionary mapping and optionally record histograms for specified columns.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - dct (dict): A dictionary mapping old values to new values.
    - columns (list, optional): A list of column names to plot histograms for. Defaults to None.
    - plot_histograms (bool, optional): Whether to plot histograms for the specified columns. Defaults to False.
    
    Returns:
    - pd.DataFrame: The DataFrame with replaced values.
    """
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame.")
    
    # Replace values in the DataFrame
    df_replaced = df.replace(dct)
    
    # Plot histograms for specified columns if required
    if plot_histograms and columns:
        for col in columns:
            if col in df_replaced.columns:
                df_replaced[col].hist()
                plt.title(f'Histogram of {col}')
                plt.xlabel(col)
                plt.ylabel('Frequency')
                plt.show()
    
    return df_replaced