import matplotlib.pyplot as plt
import random
COLORS = ['#00bfbf', '#000000', '#0000ff']
def task_func(number_list, bins):
    """
    Generates a histogram plot for a list of numbers.

    Parameters:
    number_list (list): A list of numbers to plot.
    bins (int): The number of bins to use in the histogram.

    Returns:
    matplotlib.axes._axes.Axes: The axes object representing the histogram plot.
    """
    # Randomly select a color from the predefined set
    color = random.choice(COLORS)
    
    # Create a histogram plot
    axes = plt.subplot()
    axes.hist(number_list, bins=bins, color=color)
    
    # Set the plot title and axis labels
    axes.set_title('Histogram')
    axes.set_xlabel('Number')
    axes.set_ylabel('Frequency')
    
    # Return the axes object
    return axes