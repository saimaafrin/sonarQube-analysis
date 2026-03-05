import time
import random
def task_func(iterations=5, min_delay=1.0, max_delay=2.0, seed=None):
    """
    Simulates a delay and returns a message indicating the elapsed time for a specified number of iterations.
    
    Parameters:
    iterations (int): The number of iterations to perform.
    min_delay (float): The minimum delay in seconds.
    max_delay (float): The maximum delay in seconds.
    seed (int, optional): The seed for the random number generator.
    
    Returns:
    list of str: A list of messages indicating the elapsed time for each iteration.
    float: The total amount of delay.
    
    Raises:
    ValueError: If iterations is not a positive integer or if min_delay/max_delay is not a positive floating point value.
    """
    if not isinstance(iterations, int) or iterations <= 0:
        raise ValueError("iterations must be a positive integer")
    if not (isinstance(min_delay, float) and isinstance(max_delay, float)) or min_delay <= 0 or max_delay <= 0:
        raise ValueError("min_delay and max_delay must be positive floating point values")
    
    random.seed(seed)
    messages = []
    total_delay = 0.0
    
    for _ in range(iterations):
        delay = random.uniform(min_delay, max_delay)
        time.sleep(delay)
        total_delay += delay
        messages.append(f'{delay:.2f} seconds have passed')
    
    return messages, total_delay