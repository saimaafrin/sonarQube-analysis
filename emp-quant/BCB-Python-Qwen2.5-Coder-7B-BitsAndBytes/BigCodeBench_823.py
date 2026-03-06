
import time
import numpy as np

def task_func(samples=10, delay=0.1):
    delays = []
    
    for _ in range(samples):
        start_time = time.time()
        time.sleep(delay)
        end_time = time.time()
        
        actual_delay = end_time - start_time
        delays.append(actual_delay)
    
    mean_delay = np.mean(delays)
    std_deviation = np.std(delays)
    
    return (mean_delay, std_deviation)