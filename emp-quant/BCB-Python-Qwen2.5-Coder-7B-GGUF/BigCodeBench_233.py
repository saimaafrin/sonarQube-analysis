
import random
import matplotlib.pyplot as plt

# Sample data
class Object:
    value = 0
    def __init__(self, value=None):
        if value is None:
            self.value = random.gauss(0, 1)
        else:
            self.value = value

def task_func(obj_list, attr, num_bins=30, seed=0):
    """
    Create a histogram of the specified attribute from a list of objects and return the histogram plot.

    Parameters:
    obj_list (list): List of objects.
    attr (str): The attribute to plot.
    num_bins (int): Number of bins to use in the histogram, set to 30 by default.
    seed (int): Seed for random number generator.

    Returns:
    matplotlib.axes._axes.Axes: The histogram plot of the attribute values.
    """
    # Set the seed for random number generator
    random.seed(seed)
    
    # Extract attribute values from the list of objects
    values = [getattr(obj, attr) for obj in obj_list]
    
    # Create the histogram plot
    fig, ax = plt.subplots()
    ax.hist(values, bins=num_bins, edgecolor='black')
    
    # Set the title and labels
    ax.set_title('Histogram of attribute values')
    ax.set_xlabel('Attribute Value')
    ax.set_ylabel('Count')
    
    return ax