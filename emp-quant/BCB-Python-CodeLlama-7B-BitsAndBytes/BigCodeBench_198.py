
import numpy as np
import bisect
import statistics
import matplotlib.pyplot as plt

def task_func(data, value):
    # Calculate the average of the data
    average = statistics.mean(data)

    # Identify values greater than the average
    greater_than_average = [x for x in data if x > average]

    # Count the number of values greater than the given value
    count = len(greater_than_average)

    # Plot the histogram of the sorted numbers
    plt.hist(sorted(data), bins=50)
    plt.show()

    return np.array(greater_than_average), count

greater_than_average, count = task_func(data, value)
print(greater_than_average)
print(count)