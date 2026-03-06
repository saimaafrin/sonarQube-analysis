
import time
import random

def task_func(iterations=5, min_delay=1.0, max_delay=2.0, seed=None):
    if not isinstance(iterations, int) or iterations <= 0:
        raise ValueError("iterations must be a positive integer")
    if not (isinstance(min_delay, float) and isinstance(max_delay, float)) or min_delay <= 0 or max_delay <= 0:
        raise ValueError("min_delay and max_delay must be positive floating point values")
    
    if seed is not None:
        random.seed(seed)
    
    messages = []
    total_delay = 0
    
    for _ in range(iterations):
        delay = random.uniform(min_delay, max_delay)
        time.sleep(delay)
        total_delay += delay
        messages.append(f'{delay:.2f} seconds have passed')
    
    return messages, total_delay