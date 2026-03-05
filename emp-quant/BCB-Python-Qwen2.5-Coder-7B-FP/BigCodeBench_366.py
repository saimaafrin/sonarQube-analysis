import matplotlib.pyplot as plt
import random
COLORS = ['#00bfbf', '#000000', '#0000ff']
def task_func(number_list, bins):
    """
    Generates a histogram plot for the given list of numbers.

    Parameters:
    - number_list: List of numbers to plot.
    - bins: Number of bins for the histogram.

    Returns:
    - matplotlib.axes._axes.Axes: The axes object representing the histogram plot.
    """
    # Select a random color from the predefined set
    color = random.choice(COLORS)
    
    # Create the histogram plot
    axes = plt.hist(number_list, bins=bins, color=color)
    
    # Set the plot title and axis labels
    plt.title('Histogram')
    plt.xlabel('Number')
    plt.ylabel('Frequency')
    
    # Return the axes object
    return axes