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
    This function creates a visual representation of a specified number of unique shape-color combinations, each displayed as a bar in the countplot. The shape-color pairs are selected from a predefined list.
    The function should output with:
        ax (matplotlib.axes._axes.Axes): The Axes object of the countplot, which can be used for
        further customizations or to retrieve information about the plot.
    """
    # Generate a list of shape-color pairs
    shape_color_pairs = list(itertools.product(SHAPES, COLORS))
    # Select a random subset of shape-color pairs
    random.shuffle(shape_color_pairs)
    shape_color_pairs = shape_color_pairs[:num_pairs]
    # Create a countplot
    ax = sns.countplot(x=shape_color_pairs)
    # Display the plot
    plt.show()
    return ax