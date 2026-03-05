
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, bins=20):
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    last_column = df.columns[-1]
    ax = df[last_column].hist(bins=bins, figsize=(10, 6))
    ax.set_title(f'Histogram of {last_column}')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    return ax