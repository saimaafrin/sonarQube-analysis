
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
        timestamps.append(timestamp)
        values.append(randint(0, 100))
    return (timestamps, values)

# Plot the data
plt.plot(timestamps, values)
plt.xlabel('Time')
plt.ylabel('Random Value')
plt.title('Random Data Generation')
plt.show()