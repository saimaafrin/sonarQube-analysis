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
    value (int): The value to compare against.
    
    Returns:
    numpy.ndarray: An array of values from the data that are greater than the average.
    int: The number of values in the data that are greater than the given value.
    """
    if not data:
        return np.array([]), 0
    
    # Convert list to numpy array for efficient computation
    data_array = np.array(data)
    
    # Calculate the average of the data
    average = statistics.mean(data_array)
    
    # Filter values greater than the average
    greater_than_average = data_array[data_array > average]
    
    # Count values greater than the specified value
    count_greater_than_value = np.sum(data_array > value)
    
    # Sort the data and plot the histogram
    sorted_data = np.sort(data_array)
    plt.hist(sorted_data, bins='auto', color='blue', edgecolor='black')
    plt.title('Histogram of Sorted Data')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
    
    return greater_than_average, count_greater_than_value
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
value = 5