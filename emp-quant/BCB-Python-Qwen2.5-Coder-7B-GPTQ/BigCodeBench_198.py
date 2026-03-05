import numpy as np
import bisect
import statistics
import matplotlib.pyplot as plt
def task_func(data, value):
    if not data:
        return np.array([]), 0
    
    # Calculate the average of the data
    avg = statistics.mean(data)
    
    # Filter values greater than the average
    greater_than_avg = np.array([x for x in data if x > avg])
    
    # Count values greater than the specified value
    count_greater_than_value = sum(1 for x in data if x > value)
    
    # Sort the data
    sorted_data = np.sort(data)
    
    # Plot the histogram of the sorted numbers
    plt.hist(sorted_data, bins='auto')
    plt.title('Histogram of Sorted Numbers')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
    
    return greater_than_avg, count_greater_than_value