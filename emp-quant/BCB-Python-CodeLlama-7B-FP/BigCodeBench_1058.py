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
    # Generate a list of unique shape-color pairs
    shape_color_pairs = list(itertools.product(SHAPES, COLORS))
    # Select a random subset of the pairs
    random_pairs = random.sample(shape_color_pairs, num_pairs)
    # Create a countplot of the selected pairs
    ax = sns.countplot(x="Shape", hue="Color", data=random_pairs)
    # Display the plot
    plt.show()
    return ax