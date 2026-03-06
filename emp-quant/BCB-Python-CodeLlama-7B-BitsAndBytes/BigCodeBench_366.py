
import matplotlib.pyplot as plt
import random

# Constants
COLORS = ['#00bfbf', '#000000', '#0000ff']

def task_func(number_list, bins):
    # Create a histogram plot
    fig, ax = plt.subplots()
    ax.hist(number_list, bins=bins, color=random.choice(COLORS))

    # Set plot title, x-axis label, and y-axis label
    ax.set_title('Histogram')
    ax.set_xlabel('Number')
    ax.set_ylabel('Frequency')

    # Return the axes object
    return ax

# Show the plot
plt.show()