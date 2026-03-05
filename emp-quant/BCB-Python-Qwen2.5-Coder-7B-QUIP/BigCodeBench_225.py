
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, dct, columns=None, plot_histograms=False):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame.")
    
    # Replace values in the DataFrame based on the dictionary mapping
    df = df.replace(dct)
    
    # Optionally plot histograms for specified columns
    if columns and plot_histograms:
        for col in columns:
            df[col].plot(kind='hist', bins=10, edgecolor='k')
            plt.title(f'Histogram of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.show()
    
    return df