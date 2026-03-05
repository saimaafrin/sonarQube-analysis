
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def task_func(x, y, labels):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Normal Distributions')
    ax.grid(True)
    for i in range(len(x)):
        ax.plot(stats.norm.pdf(x[i], y[i]), label=labels[i])
    ax.legend()
    return fig