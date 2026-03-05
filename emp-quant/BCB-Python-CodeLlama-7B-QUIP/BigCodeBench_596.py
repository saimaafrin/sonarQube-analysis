
import time
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt

def task_func(duration):
    start_time = time.time()
    timestamps = []
    values = []
    while time.time() - start_time < duration:
        timestamps.append(datetime.strftime(time.time(), '%H:%M:%S.%f'))
        values.append(randint(0, 100))
    return (timestamps, values)

# Generate and draw random data in real time for the specified duration
duration = 10 # seconds
timestamps, values = task_func(duration)

# Plot the data
plt.plot(timestamps, values)
plt.show()