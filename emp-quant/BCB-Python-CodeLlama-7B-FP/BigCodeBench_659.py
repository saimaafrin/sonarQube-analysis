import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
def task_func(x, y, labels):
    """
    Draw normal distributions for multiple 'x' and 'y' arrays with labels.
    Each pair (x, y) represents a different chemical compound in the 'labels' list.
    """
    fig, ax = plt.subplots()
    for i, (x_i, y_i, label_i) in enumerate(zip(x, y, labels)):
        ax.plot(x_i, y_i, label=label_i)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Normal Distributions for Chemical Compounds')
    return fig
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
labels = ['A', 'B', 'C', 'D', 'E']