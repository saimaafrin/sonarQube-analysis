
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    if df.empty:
        ax = plt.gca()
        ax.set_title('Value Distribution')
        ax.set_xlabel('Value')
        ax.set_ylabel('Count')
        return ax
    
    value_counts = df['value'].value_counts().sort_index()
    ax = value_counts.plot(kind='bar', figsize=(10, 6))
    ax.set_title('Value Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Count')
    
    return ax