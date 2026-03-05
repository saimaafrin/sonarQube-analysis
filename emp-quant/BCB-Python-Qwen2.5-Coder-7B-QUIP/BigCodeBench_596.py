
import time
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt

def task_func(duration):
    timestamps = []
    values = []
    start_time = time.time()
    
    while time.time() - start_time < duration:
        current_time = datetime.now().strftime('%H:%M:%S.%f')
        random_value = randint(0, 100)  # Generate a random value between 0 and 100
        timestamps.append(current_time)
        values.append(random_value)
        
        # Plot the data in real-time
        plt.plot(timestamps, values, marker='o', linestyle='-', color='b')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Real-time Data')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.pause(0.1)  # Pause for a short duration to update the plot
        
    return (timestamps, values)