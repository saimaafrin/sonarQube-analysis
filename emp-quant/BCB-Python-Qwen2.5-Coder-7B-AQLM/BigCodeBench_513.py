
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    if not data:
        raise ValueError("Data list is empty")
    
    df = pd.DataFrame(data)
    
    if column not in df.columns:
        raise KeyError("Invalid column name")
    
    if not all(df[column] >= 0):
        raise ValueError("Numeric values for steps, calories burned, and distance walked must be non-negative")
    
    summary_stats = {
        'sum': df[column].sum(),
        'mean': df[column].mean(),
        'min': df[column].min(),
        'max': df[column].max()
    }
    
    plt.figure(figsize=(10, 6))
    line_chart = plt.plot(df['Date'], df[column], marker='o', linestyle='-', color='b')
    plt.title(f'Line Chart of {column}')
    plt.xlabel('Date')
    plt.ylabel(column)
    plt.grid(True)
    
    return (summary_stats, line_chart)