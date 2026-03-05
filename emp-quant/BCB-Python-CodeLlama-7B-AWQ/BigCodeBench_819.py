import time
import random
def task_func(iterations=5, min_delay=1.0, max_delay=2.0, seed=None):
    """
    Simulates a delay and then returns a message indicating the elapsed time.
    This is repeated for a specified number of iterations. For each iteration the delay is randomly sampled from a uniform distribution specified by min_delay and max_delay.
    After each iteration the message: '{delay} seconds have passed', where {delay} is replaced with the actual delay of the iteration with 2 positions after the decimal point, is saved to an array.
    The function returns a list of all messages, as well as the total delay.
    """
    if not isinstance(iterations, int) or iterations < 1:
        raise ValueError("iterations must be a positive integer")
    if not isinstance(min_delay, float) or min_delay < 0:
        raise ValueError("min_delay must be a positive floating point value")
    if not isinstance(max_delay, float) or max_delay < 0:
        raise ValueError("max_delay must be a positive floating point value")

    messages = []
    total_delay = 0
    for i in range(iterations):
        delay = random.uniform(min_delay, max_delay)
        time.sleep(delay)
        messages.append(f"{delay:.2f} seconds have passed")
        total_delay += delay

    return messages, total_delay