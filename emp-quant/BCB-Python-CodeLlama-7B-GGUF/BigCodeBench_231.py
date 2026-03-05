
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
from matplotlib.axes import Axes
class ValueObject:
    value = 0
    def __init__(self, mu=0, std=1, seed=77):
        random.seed(seed)
        self.value = random.gauss(mu, std)
def task_func(obj_list) -> Axes:
    if not obj_list:
        mu = 0
        std = 0
    else:
        values = [obj.value for obj in obj_list]
        mu = np.mean(values)
        std = np.std(values)
    x = np.linspace(mu - 3 * std, mu + 3 * std, 100)
    y = stats.norm.pdf(x, mu, std)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram and Custom Normal Distribution Curve')
    return ax