
import time
import numpy as np

def task_func(samples=10, delay=0.1):
    delays = []
    for _ in range(samples):
        start_time = time.time()
        # Simulate some task
        time.sleep(delay)
        end_time = time.time()
        delays.append(end_time - start_time)
    
    mean_delay = np.mean(delays)
    std_delay = np.std(delays)
    return (mean_delay, std_delay)