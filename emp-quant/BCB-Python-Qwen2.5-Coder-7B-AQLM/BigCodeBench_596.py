
import time
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def task_func(duration):
    timestamps = []
    values = []
    
    fig, ax = plt.subplots()
    line, = ax.plot([], [], 'r-')
    ax.set_xlim(0, duration)
    ax.set_ylim(0, 100)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Random Value')
    ax.set_title('Real-time Random Data')
    
    def update(frame):
        timestamp = datetime.now().strftime('%H:%M:%S.%f')
        value = randint(0, 100)
        timestamps.append(timestamp)
        values.append(value)
        
        line.set_data(range(len(timestamps)), values)
        ax.set_xlim(0, len(timestamps))
        ax.set_ylim(min(values), max(values))
        return line,
    
    ani = animation.FuncAnimation(fig, update, frames=range(duration), interval=1000, repeat=False)
    plt.show()
    
    return (timestamps, values)