import itertools
import seaborn as sns
import matplotlib.pyplot as plt
SHAPES = [
    "Circle",
    "Square",
    "Triangle",
    "Rectangle",
    "Pentagon",
    "Hexagon",
    "Heptagon",
    "Octagon",
    "Nonagon",
    "Decagon",
]
COLORS = [
    "Red",
    "Blue",
    "Green",
    "Yellow",
    "Black",
    "White",
    "Purple",
    "Orange",
    "Pink",
    "Brown",
]
def task_func(num_pairs=10):
    """
    Generate and display a countplot of predefined shape-color pairs.

    This function creates a visual representation of a specified number of unique shape-color combinations,
    each displayed as a bar in the countplot. The shape-color pairs are selected from a predefined list.

    Parameters:
    - num_pairs (int): The number of unique shape-color pairs to be displayed in the countplot.
                       Default is 10. If the requested number is less than 1 or greater than the total
                       possible unique combinations (100), it is adjusted to the valid range (1 to 100).

    Returns:
    - ax (matplotlib.axes._axes.Axes): The Axes object of the countplot, which can be used for
                                                  further customizations or to retrieve information about the plot.

    Requirements:
    - itertools
    - seaborn
    - matplotlib

    Example:
    >>> ax = task_func(10)
    >>> [tick.get_text() for tick in ax.get_xticklabels()]
    ['Circle:Red', 'Circle:Blue', 'Circle:Green', 'Circle:Yellow', 'Circle:Black', 'Circle:White', 'Circle:Purple', 'Circle:Orange', 'Circle:Pink', 'Circle:Brown']
    >>> ax = task_func(9)
    >>> [tick.get_text() for tick in ax.get_xticklabels()]
    ['Circle:Red', 'Circle:Blue', 'Circle:Green', 'Circle:Yellow', 'Circle:Black', 'Circle:White', 'Circle:Purple', 'Circle:Orange', 'Circle:Pink', 'Circle:Brown']
    >>> ax = task_func(8)
    >>> [tick.get_text() for tick in ax.get_xticklabels()]
    ['Circle:Red', 'Circle:Blue', 'Circle:Green', 'Circle:Yellow', 'Circle:Black', 'Circle:White', 'Circle:Purple', 'Circle:Orange', 'Circle:Pink', 'Circle:Brown']
    >>> ax = task_func(7)
    >>> [tick.get_text() for tick in ax.get_xticklabels()]
    ['Circle:Red', 'Circle:Blue', 'Circle:Green', 'Circle:Yellow', 'Circle:Black', 'Circle:White', 'Circle:Purple', 'Circle:Orange', 'Circle:Pink', 'Circle:Brown']
    >>> ax = task_func(6)
    >>> [tick.get_text() for tick in ax.get_xticklabels()]
    ['Circle:Red', 'Circle:Blue', 'Circle:Green', 'Circle:Yellow', 'Circle:Black', 'Circle:White', 'Circle:Purple', 'Circle:Orange', 'Circle:Pink', 'Circle:Brown']
    """
    # Adjust the number of pairs to the valid range
    num_pairs = max(1, min(num_pairs, len(SHAPES) * len(COLORS)))

    # Create a list of shape-color pairs
    pairs = list(itertools.product(SHAPES, COLORS))

    # Select the first num_pairs pairs
    pairs = pairs[:num_pairs]

    # Create a countplot of the pairs
    ax = sns.countplot(x=pairs)

    # Set the x-axis labels
    ax.set_xticklabels([f"{shape}:{color}" for shape, color in pairs])

    # Set the x-axis title
    ax.set_xlabel("Shape-Color Pairs")

    # Set the y-axis title
    ax.set_ylabel("Count")

    # Set the title
    ax.set_title("Shape-Color Pairs Countplot")

    # Return the Axes object of the countplot
    return ax