
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def task_func(x, y, labels):
    fig, axs = plt.subplots(len(labels), 1, figsize=(8, len(labels)*2))
    
    for ax, (xi, yi, label) in zip(axs, zip(x, y, labels)):
        ax.plot(xi, yi, 'o')
        ax.set_title(f'Distribution of {label}')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.grid(True)
    
    plt.tight_layout()
    return fig