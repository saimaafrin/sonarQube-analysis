
import itertools
import seaborn as sns
import matplotlib.pyplot as plt
# Constants
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
    # Generate a list of shape-color pairs
    shape_color_pairs = itertools.product(SHAPES, COLORS)
    # Create a countplot of the shape-color pairs
    ax = sns.countplot(shape_color_pairs)
    # Display the countplot
    plt.show()
    return ax