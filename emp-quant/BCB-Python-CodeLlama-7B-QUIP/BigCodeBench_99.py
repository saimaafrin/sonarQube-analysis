
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

def task_func():
    # Load the iris dataset
    iris = load_iris()

    # Set the global font to Arial
    plt.rcParams['font.family'] = 'Arial'

    # Create a figure object
    fig = plt.Figure(figsize=(8, 8))

    # Create a seaborn pair plot
    g = sns.pairplot(iris.data, hue='species', size=20, aspect=2, plot_hue=False)

    # Set the title of the plot
    g.set_title('Iris Dataset Pair Plot')

    # Set the labels for the axes
    g.set_xlabel('Feature 1')
    g.set_ylabel('Feature 2')

    # Set the labels for the subplots
    g.set_xticklabels(g.axes.flatten()[0].get_xlabel())
    g.set_yticklabels(g.axes.flatten()[0].get_ylabel())

    # Set the labels for the legend
    g.legend(title='Species')

    # Show the plot
    plt.show()

    return fig