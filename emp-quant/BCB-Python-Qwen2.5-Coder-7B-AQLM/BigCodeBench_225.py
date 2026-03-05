
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, dct, columns=None, plot_histograms=False):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame.")
    
    if columns is None:
        columns = df.columns
    
    df_replaced = df.copy()
    for col in columns:
        if col in df_replaced.columns:
            df_replaced[col] = df_replaced[col].map(dct)
    
    if plot_histograms:
        for col in columns:
            if col in df_replaced.columns:
                df_replaced[col].hist(bins=10)
                plt.title(f'Histogram of {col}')
                plt.xlabel(col)
                plt.ylabel('Frequency')
                plt.show()
    
    return df_replaced