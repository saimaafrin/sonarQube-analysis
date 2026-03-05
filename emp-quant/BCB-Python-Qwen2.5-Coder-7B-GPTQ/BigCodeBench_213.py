import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis
def task_func(intervals=100, seed=0):
    random.seed(seed)
    time_series = []
    elapsed_times = []
    start_time = time.time()
    
    for _ in range(intervals):
        time.sleep(1)  # Delay of 1 second between intervals
        current_time = time.time()
        elapsed_time = current_time - start_time
        elapsed_times.append(elapsed_time)
        time_series.append(random.random())
    
    plt.figure()
    plt.plot(elapsed_times, time_series)
    plt.xlabel('Elapsed Time (seconds)')
    plt.ylabel('Random Number')
    plt.title('Random Number Series Over Time')
    plt.show()
    
    kurtosis_value = kurtosis(time_series)
    return plt.gca(), kurtosis_value