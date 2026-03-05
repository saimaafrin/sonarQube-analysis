
import time
import random

def task_func(iterations=5, min_delay=1.0, max_delay=2.0, seed=None):
    if iterations <= 0:
        raise ValueError("Iterations must be a positive integer")
    if min_delay <= 0 or max_delay <= 0:
        raise ValueError("Min and max delay must be positive floating point values")
    if seed is not None:
        random.seed(seed)
    messages = []
    delay = 0
    for i in range(iterations):
        delay += random.uniform(min_delay, max_delay)
        messages.append(f"{delay:.2f} seconds have passed")
    return messages, delay