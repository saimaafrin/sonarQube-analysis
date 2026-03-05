
import time
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt

def task_func(duration):
    start_time = time.time()
    timestamps = []
    values = []
    while time.time() - start_time < duration:
        timestamp = datetime.now().strftime('%H:%M:%S.%f')
        value = randint(0, 100)
        timestamps.append(timestamp)
        values.append(value)
    return (timestamps, values)