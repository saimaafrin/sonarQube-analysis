
import bisect
import statistics
import numpy as np
import matplotlib.pyplot as plt

def task_func(df, column, value):
    # Check if the column exists in the DataFrame
    if column not in df.columns:
        raise ValueError("Column does not exist in the DataFrame")
    
    # Check if the value is a number
    if not isinstance(value, (int, float)):
        raise ValueError("Value is not a number")
    
    # Calculate the average of the column
    avg = statistics.mean(df[column])
    
    # Filter values greater than the average
    greater_than_avg = df[column][df[column] > avg].values
    
    # Count values greater than the given value
    count_greater_than_value = (df[column] > value).sum()
    
    # Plot histogram
    fig, ax = plt.subplots()
    df[column].hist(ax=ax)
    ax.set_title(f"Histogram of {column}")
    
    return greater_than_avg, count_greater_than_value, ax