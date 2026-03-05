import bisect
import statistics
import matplotlib.pyplot as plt
import numpy as np
def task_func(df, column, value):
    # Check if the column exists in the DataFrame
    if column not in df.columns:
        raise ValueError("Column does not exist in the DataFrame")
    
    # Check if the value is a number
    if not isinstance(value, (int, float)):
        raise ValueError("Value is not a number")
    
    # Calculate the average of the column
    avg = statistics.mean(df[column])
    
    # Find values greater than the average
    greater_than_avg = df[column][df[column] > avg].values
    
    # Count the number of values greater than the given value
    count_greater_than_value = bisect.bisect_right(greater_than_avg, value)
    
    # Generate a histogram plot
    fig, ax = plt.subplots()
    df[column].hist(ax=ax)
    ax.axvline(x=avg, color='r', linestyle='--', label='Average')
    ax.axvline(x=value, color='g', linestyle='--', label=f'Value: {value}')
    ax.legend()
    
    return greater_than_avg, count_greater_than_value, ax