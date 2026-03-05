
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
    # Generate a list of unique shape-color pairs
    shape_color_pairs = list(itertools.product(SHAPES, COLORS))
    
    # Select a subset of the pairs based on num_pairs
    selected_pairs = shape_color_pairs[:num_pairs]
    
    # Create a countplot using seaborn
    ax = sns.countplot(x=[pair[0] for pair in selected_pairs], palette=[pair[1] for pair in selected_pairs])
    
    # Set the title and labels
    ax.set_title('Shape-Color Countplot')
    ax.set_xlabel('Shape')
    ax.set_ylabel('Color')
    
    # Display the plot
    plt.show()
    
    # Return the Axes object
    return ax