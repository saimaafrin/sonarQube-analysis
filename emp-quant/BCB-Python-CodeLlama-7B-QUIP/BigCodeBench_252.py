
import matplotlib.pyplot as plt
from itertools import zip_longest
# Constants
COLORS = ['red', 'green', 'blue', 'yellow', 'purple']
def task_func(data, labels):
    # Create figure and axis
    fig, ax = plt.subplots()
    # Plot data
    for i, (data_series, label) in enumerate(zip_longest(data, labels, fillvalue='black')):
        ax.plot(data_series, label=label)
        if i >= len(COLORS):
            ax.set_prop_cycle(color=COLORS[i % len(COLORS)])
    return ax