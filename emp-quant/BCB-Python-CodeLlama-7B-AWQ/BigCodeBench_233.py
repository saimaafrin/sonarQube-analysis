import random
import matplotlib.pyplot as plt
def task_func(obj_list, attr, num_bins=30, seed=0):
    """
    Create a histogram of the specified attribute from a list of objects and return the histogram plot.
    Constants:
    - NUM_BINS (int): Number of bins to use in the histogram, set to 30 by default.
    The function should output with:
        matplotlib.axes._axes.Axes: The histogram plot of the attribute values, with the title 'Histogram of attribute values', x-axis labeled 'Attribute Value', and y-axis labeled 'Count'.
    """
    # Set random seed for reproducibility
    random.seed(seed)

    # Extract attribute values from objects
    values = [getattr(obj, attr) for obj in obj_list]

    # Create histogram
    counts, bins = np.histogram(values, bins=num_bins)

    # Create plot
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], counts, width=bins[1]-bins[0])
    ax.set_title('Histogram of attribute values')
    ax.set_xlabel('Attribute Value')
    ax.set_ylabel('Count')
    return ax