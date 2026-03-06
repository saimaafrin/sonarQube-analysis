
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

def task_func(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    day_of_month = date.day
    frequency = 10 * (day_of_month - 1)
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(frequency * x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.set_title('Sine Wave with Frequency Determined by Day of Month')
    return ax