
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
    # Generate unique shape-color pairs
    shape_color_pairs = list(itertools.product(SHAPES, COLORS))
    selected_pairs = shape_color_pairs[:num_pairs]
    
    # Create a DataFrame for the selected pairs
    df = pd.DataFrame(selected_pairs, columns=["Shape", "Color"])
    
    # Create a countplot
    ax = sns.countplot(x="Shape", y="Color", data=df)
    
    # Display the plot
    plt.show()
    
    return ax