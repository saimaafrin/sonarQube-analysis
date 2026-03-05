
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def task_func(x, y, labels):
    fig, ax = plt.subplots()
    for i in range(len(x)):
        ax.plot(x[i], y[i], label=labels[i])
        ax.axvline(x[i].mean(), color='r', linestyle='--')
        ax.axhline(y[i].mean(), color='r', linestyle='--')
    ax.legend()
    return fig