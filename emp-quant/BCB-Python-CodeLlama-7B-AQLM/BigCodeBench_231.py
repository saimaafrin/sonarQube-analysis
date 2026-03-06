import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
from matplotlib.axes import Axes
def task_func(obj_list) -> Axes:
    '''
    Draw the histogram and the custom normal distribution curve from the mean and standard deviation
    derived from the values of a list of ValueObjects and return the plotted Axes. For an empty list,
    the mean and the standard deviation is 0.
    
    Parameters:
    obj_list (list): The list of objects.
    attr (str): The attribute to plot.

    Returns:
    Axes: The plotted Axes.

    Requirements:
    - numpy
    - scipy.stats
    - matplotlib
    - random

    Example:
    >>> obj_list = [ValueObject(mu=23, std=77), ValueObject(mu=23, std=77, seed=222), ValueObject(mu=23, std=77, seed=333)]
    >>> ax = task_func(obj_list)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    '''
    if len(obj_list) == 0:
        mu = 0
        std = 0
    else:
        mu = np.mean([obj.value for obj in obj_list])
        std = np.std([obj.value for obj in obj_list])

    ax = plt.hist(
        [obj.value for obj in obj_list],
        bins=100,
        density=True,
        histtype='bar',
        color='#000000',
        edgecolor='#000000',
        linewidth=1,
        alpha=0.5,
        label='Histogram'
    )
    x = np.linspace(mu - 3 * std, mu + 3 * std, 100)
    y = stats.norm.pdf(x, mu, std)
    ax.plot(x, y, color='#000000', linewidth=1, label='Normal distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability')
    ax.set_title('Histogram and normal distribution')
    ax.legend()
    return ax