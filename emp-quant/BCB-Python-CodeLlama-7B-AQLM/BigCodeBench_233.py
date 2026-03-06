import random
import matplotlib.pyplot as plt
def task_func(obj_list, attr, num_bins=30, seed=0):
    """
    Create a histogram of the specified attribute from a list of objects and return the histogram plot.

    Parameters:
    obj_list (list): The list of objects containing the attribute.
    attr (str): The attribute to generate a histogram for.
    num_bins (int, Optional): The number of bins to use in the histogram. Defaults to 30.
    seed (int, Optional): The seed for the random number generator. Defaults to 0.

    Returns:
    matplotlib.axes._axes.Axes: The histogram plot of the attribute values, with the title 'Histogram of attribute values', x-axis labeled 'Attribute Value', and y-axis labeled 'Count'.

    Requirements:
    - random (used for default object generation)
    - numpy (used for numerical computations)
    - matplotlib (used for plotting)

    Constants:
    - NUM_BINS (int): Number of bins to use in the histogram, set to 30 by default.

    Example:
    >>> obj_list = [Object(value=i) for i in range(10)]
    >>> ax = task_func(obj_list, 'value')
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    random.seed(seed)
    values = [getattr(obj, attr) for obj in obj_list]
    values = sorted(values)
    bins = [values[i] for i in range(len(values)) if i % num_bins == 0]
    counts = [values.count(b) for b in bins]
    plt.hist(values, bins=bins, weights=counts)
    plt.title('Histogram of attribute values')
    plt.xlabel('Attribute Value')
    plt.ylabel('Count')
    return plt.gca()