
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
        random_value = randint(0, 100)
        
        timestamps.append(current_time)
        values.append(random_value)
        
        # Clear the previous plot and redraw it
        plt.clf()
        plt.plot(timestamps, values, marker='o', linestyle='-')
        plt.xlabel('Time')
        plt.ylabel('Random Value')
        plt.title('Real-Time Random Data')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.pause(0.1)
    
    return (timestamps, values)