
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
    # Generate all possible shape-color pairs
    pairs = list(itertools.product(SHAPES, COLORS))
    
    # Select the first 'num_pairs' unique pairs
    selected_pairs = pairs[:num_pairs]
    
    # Create a DataFrame for plotting
    df = pd.DataFrame(selected_pairs, columns=['Shape', 'Color'])
    
    # Create a countplot using seaborn
    ax = sns.countplot(x='Shape', data=df)
    
    # Set title and labels
    ax.set_title(f"Count of Shape-Color Pairs ({num_pairs} pairs)")
    ax.set_xlabel('Shape')
    ax.set_ylabel('Count')
    
    # Show the plot
    plt.show()
    
    return ax