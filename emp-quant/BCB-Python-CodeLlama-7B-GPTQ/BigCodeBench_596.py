import time
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
def task_func(duration):
    """
    Generate and draw random data in real time for the specified duration.
    The function should output with:
        tuple: A tuple containing two lists.
        The first list contains timestamps (as strings) in the format '%H:%M:%S.%f'.
        The second list contains the generated random values.
    """
    start_time = time.time()
    end_time = start_time + duration
    timestamps = []
    values = []
    while time.time() < end_time:
        timestamp = datetime.now().strftime('%H:%M:%S.%f')
        value = randint(0, 100)
        timestamps.append(timestamp)
        values.append(value)
    return (timestamps, values)
duration = 10