
import numpy as np
import math
import matplotlib.pyplot as plt

def task_func(range_start=0, range_end=10, step=0.1):
    x = np.arange(range_start, range_end, step)
    y = np.exp(x)
    return x, y

def plot_func(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('x')
    ax.set_ylabel('e^x')
    ax.set_title('Exponential Function')
    return fig