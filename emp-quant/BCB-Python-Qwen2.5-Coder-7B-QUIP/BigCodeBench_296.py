
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame")
    
    if df.empty:
        fig, ax = plt.subplots()
        ax.set_title("Value Distribution")
        ax.set_xlabel("Value")
        ax.set_ylabel("Count")
        return ax
    
    value_counts = df['value'].value_counts()
    fig, ax = plt.subplots()
    ax.bar(value_counts.index, value_counts.values)
    ax.set_title("Value Distribution")
    ax.set_xlabel("Value")
    ax.set_ylabel("Count")
    
    return ax