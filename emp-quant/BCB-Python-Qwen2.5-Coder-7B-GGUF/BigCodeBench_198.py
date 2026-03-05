
import numpy as np
import bisect
import statistics
import matplotlib.pyplot as plt

def task_func(data, value):
    if not data:
        return np.array([]), 0
    
    data_sorted = sorted(data)
    average = statistics.mean(data_sorted)
    greater_than_average = [x for x in data_sorted if x > average]
    
    count_greater_than_value = bisect.bisect_right(data_sorted, value)
    
    plt.hist(data_sorted, bins='auto', color='blue', alpha=0.7)
    plt.axvline(x=average, color='red', linestyle='dashed', linewidth=2, label='Average')
    plt.axvline(x=value, color='green', linestyle='dashed', linewidth=2, label=f'Value: {value}')
    plt.legend()
    plt.show()
    
    return np.array(greater_than_average), count_greater_than_value