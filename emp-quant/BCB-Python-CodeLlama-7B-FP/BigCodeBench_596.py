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
    timestamps = []
    values = []
    while time.time() - start_time < duration:
        timestamps.append(datetime.now().strftime('%H:%M:%S.%f'))
        values.append(randint(0, 100))
        time.sleep(0.01)
    return (timestamps, values)
duration = 10