import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
from matplotlib.axes import Axes
def task_func(obj_list) -> Axes:
    if not obj_list:
        mean = 0
        std = 0
    else:
        values = [obj.value for obj in obj_list]
        mean = np.mean(values)
        std = np.std(values)
    x = np.linspace(mean - 3*std, mean + 3*std, 100)
    y = stats.norm.pdf(x, mean, std)
    fig, ax = plt.subplots()
    ax.hist(values, bins=30, density=True, alpha=0.6, color='g')
    ax.plot(x, y, 'r-', lw=2)
    return ax