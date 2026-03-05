
import time
import numpy as np

def task_func(samples=10, delay=0.1):
    start_time = time.time()
    delay_times = []
    for i in range(samples):
        start_time = time.time()
        delay_times.append(time.time() - start_time)
    mean = np.mean(delay_times)
    std = np.std(delay_times)
    return (mean, std)