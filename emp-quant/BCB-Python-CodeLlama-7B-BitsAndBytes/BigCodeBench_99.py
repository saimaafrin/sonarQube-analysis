
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

def task_func():
    # Load the iris dataset
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target_names[iris.target]

    # Set the global font to Arial
    plt.rcParams['font.family'] = 'Arial'

    # Create a seaborn pair plot of the iris dataset
    g = sns.pairplot(data=df, hue='species')

    # Add a title to the plot
    g.fig.suptitle('Iris Dataset Pair Plot', fontsize=16)

    # Add labels to the axes
    g.fig.text(0.5, 0.04, 'Sepal Length (cm)', ha='center')
    g.fig.text(0.04, 0.5, 'Sepal Width (cm)', va='center', rotation='vertical')
    g.fig.text(0.5, 0.96, 'Petal Length (cm)', ha='center')
    g.fig.text(0.96, 0.5, 'Petal Width (cm)', va='center', rotation='vertical')

    # Return the matplotlib Figure object
    return g.fig

# Call the function and display the plot
task_func()