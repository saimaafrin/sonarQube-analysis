from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
def task_func(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    day = date.day
    frequency = 10 * (day - 1)
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(frequency * x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title('Sine Wave')
    return ax