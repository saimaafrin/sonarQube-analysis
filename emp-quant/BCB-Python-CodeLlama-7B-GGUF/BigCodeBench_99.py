
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

def task_func():
    # Load the iris dataset
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target

    # Set the global font to Arial
    plt.rcParams['font.family'] = 'Arial'

    # Generate the pair plot
    g = sns.pairplot(df, hue='species')

    # Add the title and axis labels
    g.fig.suptitle('Iris Dataset Pair Plot', fontsize=16)
    g.fig.text(0.5, 0.04, 'Sepal Length (cm)', ha='center')
    g.fig.text(0.5, 0.5, 'Sepal Width (cm)', va='center')
    g.fig.text(0.04, 0.5, 'Petal Length (cm)', va='center')
    g.fig.text(0.5, 0.96, 'Petal Width (cm)', ha='center')

    # Return the figure object
    return g.fig

# Call the function
task_func()