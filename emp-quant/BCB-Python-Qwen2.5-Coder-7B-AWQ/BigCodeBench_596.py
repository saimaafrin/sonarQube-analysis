import time
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
def task_func(duration):
    timestamps = []
    values = []
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        current_time = datetime.now().strftime('%H:%M:%S.%f')
        random_value = randint(0, 100)  # Generating a random value between 0 and 100
        timestamps.append(current_time)
        values.append(random_value)
        time.sleep(0.1)  # Sleep for 0.1 seconds to simulate real-time data generation

    return (timestamps, values)
duration = 10