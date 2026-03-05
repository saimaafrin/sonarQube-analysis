
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def task_func(x, y, labels):
    fig, ax = plt.subplots()
    for i in range(len(x)):
        ax.plot(x[i], y[i], label=labels[i])
    ax.legend()
    return fig