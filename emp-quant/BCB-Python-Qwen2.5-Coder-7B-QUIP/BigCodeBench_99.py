
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

def task_func():
    # Load the iris dataset
    iris = load_iris()
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    iris_df['species'] = pd.Categorical(iris.target, categories=iris.target_names, ordered=True)
    
    # Set the global font to Arial
    plt.rcParams['font.sans-serif'] = 'Arial'
    
    # Create a seaborn pair plot
    g = sns.pairplot(iris_df, hue='species', s=100, markers='o', legend=False)
    
    # Set the plot title
    g.fig.suptitle('Iris Dataset Pair Plot')
    
    # Add a legend
    g.fig.legend(labels=iris.target_names, title='Species', loc='upper right')
    
    # Show the plot
    plt.show()
    
    # Return the figure object
    return g.fig