
import numpy as np
import bisect
import statistics
import matplotlib.pyplot as plt

def task_func(data, value):
    if len(data) == 0:
        return np.array([]), 0
    average = statistics.mean(data)
    greater_than_average = np.array([x for x in data if x > average])
    count = len(greater_than_average)
    return greater_than_average, count

# Plot the histogram of the sorted numbers
data_sorted = np.sort(data)
plt.hist(data_sorted, bins=50)
plt.show()