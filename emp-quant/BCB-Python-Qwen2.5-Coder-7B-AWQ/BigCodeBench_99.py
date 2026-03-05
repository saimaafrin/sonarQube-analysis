import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
def task_func():
    # Load the iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    
    # Set the global font to Arial
    plt.rcParams['font.family'] = 'Arial'
    
    # Create a pair plot
    g = sns.pairplot(df, hue='species')
    
    # Set the title of the plot
    g.fig.suptitle('Iris Dataset Pair Plot')
    
    # Return the matplotlib Figure object
    return g.fig