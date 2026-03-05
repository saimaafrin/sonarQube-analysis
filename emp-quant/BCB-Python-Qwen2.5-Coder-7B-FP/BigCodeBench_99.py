import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
def task_func():
    # Load the iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target_names[iris.target]

    # Set the global font to Arial
    plt.rcParams['font.family'] = 'Arial'

    # Create a pair plot
    pair_plot = sns.pairplot(df, hue='species')

    # Set the title of the plot
    pair_plot.fig.suptitle('Iris Dataset Pair Plot')

    # Return the matplotlib Figure object
    return pair_plot.fig