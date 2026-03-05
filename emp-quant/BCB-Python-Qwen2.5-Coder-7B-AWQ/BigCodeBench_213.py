import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis
def task_func(intervals=100, seed=0):
    random.seed(seed)
    x_values = []
    y_values = []
    start_time = time.time()
    
    for _ in range(intervals):
        x_values.append(time.time() - start_time)
        y_values.append(random.random())
        time.sleep(1)
    
    plt.figure()
    ax = plt.plot(x_values, y_values)
    plt.xlabel('Elapsed Time (seconds)')
    plt.ylabel('Random Number')
    plt.title('Random Number Series Over Time')
    
    kurt = kurtosis(y_values)
    return ax[0], kurt