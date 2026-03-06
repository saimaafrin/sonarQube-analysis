
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

def set_global_font(font_name):
    """
    Sets the global font for all text elements in plots to the specified font name.
    
    Args:
    font_name (str): The name of the font to be used globally.
    """
    plt.rcParams['font.family'] = font_name

def task_func():
    # Load the iris dataset
    iris_data = load_iris()
    df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df['species'] = iris_data.target
    
    # Set the global font to Arial
    set_global_font('Arial')
    
    # Create a pair plot
    g = sns.pairplot(df, hue='species', palette='Set1')
    
    # Set the title of the plot
    g.fig.suptitle('Iris Dataset Pair Plot', y=1.02)
    
    # Return the figure object
    return g.fig