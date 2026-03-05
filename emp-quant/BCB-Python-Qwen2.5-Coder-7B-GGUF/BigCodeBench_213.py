
import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis

def task_func(intervals=100, seed=0):
    random.seed(seed)
    time_values = []
    number_values = []
    
    for i in range(intervals):
        time_values.append(i)
        number_values.append(random.random())
        time.sleep(1)
    
    fig, ax = plt.subplots()
    ax.plot(time_values, number_values)
    plt.show()
    
    kurtosis_value = kurtosis(number_values)
    return ax, kurtosis_value