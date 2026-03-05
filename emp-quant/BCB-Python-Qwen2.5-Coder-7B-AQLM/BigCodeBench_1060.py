
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame, column_name: str) -> (str, plt.Axes):
    if df.empty or column_name not in df.columns or df[column_name].isnull().all():
        plt.figure()
        plt.title(f"Distribution of values in {column_name} (No Data)")
        return "The DataFrame is empty or the specified column has no data.", plt.gca()
    
    value_counts = df[column_name].value_counts()
    is_uniform = value_counts.max() / value_counts.min() <= 1.1
    
    plt.figure()
    plt.bar(value_counts.index, value_counts.values, edgecolor='black', alpha=0.7)
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of values in {column_name}")
    
    if is_uniform:
        return "The distribution of values is uniform.", plt.gca()
    else:
        return "The distribution of values is not uniform.", plt.gca()