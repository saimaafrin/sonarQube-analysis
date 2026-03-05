
import time
import random

def task_func(iterations=5, min_delay=1.0, max_delay=2.0, seed=None):
    if not isinstance(iterations, int) or iterations <= 0:
        raise ValueError("Iterations must be a positive integer.")
    if not isinstance(min_delay, float) or min_delay <= 0:
        raise ValueError("Min delay must be a positive floating point value.")
    if not isinstance(max_delay, float) or max_delay <= 0:
        raise ValueError("Max delay must be a positive floating point value.")

    messages = []
    total_delay = 0.0
    for i in range(iterations):
        delay = random.uniform(min_delay, max_delay)
        elapsed_time = time.time() + delay
        messages.append(f"{delay:.2f} seconds have passed")
        total_delay += delay

    return messages, total_delay