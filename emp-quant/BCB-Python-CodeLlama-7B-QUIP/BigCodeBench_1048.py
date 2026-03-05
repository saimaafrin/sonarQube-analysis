
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

def task_func(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    day_of_month = date.day
    frequency = 2 * np.pi * day_of_month
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x * frequency)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    return ax