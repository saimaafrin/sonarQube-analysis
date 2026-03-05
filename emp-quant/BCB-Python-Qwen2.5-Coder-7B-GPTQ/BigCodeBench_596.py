import time
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
def task_func(duration):
    timestamps = []
    values = []
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=duration)
    
    while datetime.now() < end_time:
        current_time = datetime.now()
        timestamp = current_time.strftime('%H:%M:%S.%f')
        value = randint(0, 100)  # Generate a random value between 0 and 100
        timestamps.append(timestamp)
        values.append(value)
        time.sleep(0.1)  # Sleep for 0.1 seconds to simulate real-time data generation
    
    return timestamps, values
duration = 10