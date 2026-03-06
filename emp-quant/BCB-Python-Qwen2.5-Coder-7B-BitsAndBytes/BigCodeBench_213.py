
import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis

def task_func(intervals=100, seed=0):
    random.seed(seed)
    x_values = []
    y_values = []
    start_time = time.time()
    
    for i in range(intervals):
        x_values.append(time.time() - start_time)
        y_values.append(random.random())
        time.sleep(1)
    
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    plt.show(block=False)
    
    kurt = kurtosis(y_values)
    return ax, kurt