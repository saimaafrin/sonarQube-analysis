
import numpy as np
import bisect
import statistics
import matplotlib.pyplot as plt

def task_func(data, value):
    if not data:
        return np.array([]), 0

    data = np.array(data)
    avg = np.mean(data)
    greater_than_avg = data[data > avg]
    count_greater_than_value = np.sum(greater_than_avg > value)

    plt.hist(data, bins=10, edgecolor='k')
    plt.axvline(avg, color='r', linestyle='--')
    plt.show()

    return greater_than_avg, count_greater_than_value