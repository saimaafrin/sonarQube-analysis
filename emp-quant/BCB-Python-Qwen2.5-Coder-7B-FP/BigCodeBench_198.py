import numpy as np
import bisect
import statistics
import matplotlib.pyplot as plt
def task_func(data, value):
    """
    Analyzes a list of numerical data, identifies values greater than the average,
    and counts how many values are greater than a specified value. Additionally,
    plots the histogram of the sorted numbers.
    
    Parameters:
    data (list): A list of numerical data.
    value (int): The specified value to compare against.
    
    Returns:
    numpy.ndarray: An array of values from the data that are greater than the average.
    int: The number of values in the data that are greater than the given value.
    """
    if not data:
        return np.array([]), 0
    
    data_sorted = sorted(data)
    avg = statistics.mean(data_sorted)
    greater_than_avg = np.array([x for x in data_sorted if x > avg])
    count_greater_than_value = bisect.bisect_right(data_sorted, value)
    
    plt.hist(data_sorted, bins='auto', color='blue', edgecolor='black')
    plt.title('Histogram of Sorted Numbers')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
    
    return greater_than_avg, count_greater_than_value
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
value = 5