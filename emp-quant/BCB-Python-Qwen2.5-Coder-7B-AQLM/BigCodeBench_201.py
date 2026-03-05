
import bisect
import statistics
import numpy as np
import matplotlib.pyplot as plt

def task_func(df, column, value):
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    if not isinstance(value, (int, float)):
        raise ValueError(f"Value '{value}' is not a number.")
    
    column_data = df[column]
    average = statistics.mean(column_data)
    greater_than_average = column_data[column_data > average]
    
    count_greater_than_value = bisect.bisect_right(greater_than_average, value)
    
    fig, ax = plt.subplots()
    ax.hist(column_data, bins=30, edgecolor='black')
    ax.axvline(x=average, color='r', linestyle='--', label='Average')
    ax.axvline(x=value, color='g', linestyle='--', label=f'Value: {value}')
    ax.legend()
    
    return (greater_than_average.values, count_greater_than_value, ax)