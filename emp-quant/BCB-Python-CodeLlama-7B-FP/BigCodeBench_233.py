import random
import matplotlib.pyplot as plt
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

    Args:
        obj_list (list): List of objects
        attr (str): Attribute to be used for the histogram
        num_bins (int, optional): Number of bins to use in the histogram. Defaults to 30.
        seed (int, optional): Random seed for reproducibility. Defaults to 0.

    Returns:
        matplotlib.axes._axes.Axes: The histogram plot of the attribute values, with the title 'Histogram of attribute values', x-axis labeled 'Attribute Value', and y-axis labeled 'Count'.
    """
    # Set random seed for reproducibility
    random.seed(seed)

    # Extract attribute values from objects
    values = [getattr(obj, attr) for obj in obj_list]

    # Create histogram
    counts, bins = np.histogram(values, bins=num_bins)

    # Plot histogram
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], counts, width=bins[1] - bins[0])
    ax.set_title('Histogram of attribute values')
    ax.set_xlabel('Attribute Value')
    ax.set_ylabel('Count')
    return ax
obj_list = [Object() for _ in range(100)]
attr = 'value'
num_bins = 30
seed = 0