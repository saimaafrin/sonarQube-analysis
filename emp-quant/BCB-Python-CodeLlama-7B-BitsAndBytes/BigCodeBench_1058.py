
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
    shape_color_pairs = list(itertools.product(SHAPES, COLORS))

    # Create a countplot of the shape-color pairs
    ax = sns.countplot(data=shape_color_pairs)

    # Customize the plot
    ax.set_xlabel("Shape-Color Pairs")
    ax.set_ylabel("Count")
    ax.set_title("Shape-Color Pairs Countplot")

    # Display the plot
    plt.show()

# Call the function with a specified number of shape-color pairs
task_func(num_pairs=10)