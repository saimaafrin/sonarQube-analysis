
import matplotlib.pyplot as plt
import random

# Constants
COLORS = ['#00bfbf', '#000000', '#0000ff']

def task_func(number_list, bins):
    # Create a histogram plot
    ax = plt.subplot(111)
    ax.hist(number_list, bins=bins, color=random.choice(COLORS))
    ax.set_xlabel('Number')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram')
    return ax