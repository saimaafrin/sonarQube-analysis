
import numpy as np
import bisect
import statistics
import matplotlib.pyplot as plt

def task_func(data, value):
    if not data:
        return np.array([]), 0
    
    # Calculate the average of the data
    avg = statistics.mean(data)
    
    # Filter out values greater than the average
    greater_than_avg = [x for x in data if x > avg]
    
    # Count how many values are greater than the specified value
    count_greater_than_value = sum(1 for x in data if x > value)
    
    # Sort the data
    sorted_data = sorted(data)
    
    # Plot the histogram of the sorted numbers
    plt.hist(sorted_data, bins='auto', color='blue', edgecolor='black')
    plt.title('Histogram of Sorted Data')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
    
    return np.array(greater_than_avg), count_greater_than_value