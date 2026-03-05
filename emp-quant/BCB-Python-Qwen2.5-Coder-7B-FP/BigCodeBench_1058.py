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

    Parameters:
    num_pairs (int): The number of unique shape-color combinations to display.

    Returns:
    ax (matplotlib.axes._axes.Axes): The Axes object of the countplot.
    """
    # Generate unique shape-color pairs
    shape_color_pairs = list(itertools.product(SHAPES, COLORS))[:num_pairs]
    
    # Create a DataFrame from the pairs
    df = pd.DataFrame(shape_color_pairs, columns=["Shape", "Color"])
    
    # Create a countplot
    ax = sns.countplot(x="Shape", hue="Color", data=df)
    
    # Display the plot
    plt.show()
    
    return ax