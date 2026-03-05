
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    if df.empty:
        return None
    value_counts = df['value'].value_counts()
    ax = plt.bar(value_counts.index, value_counts.values, label='Value Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Count')
    return ax