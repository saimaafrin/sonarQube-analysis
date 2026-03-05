
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def task_func(data_url="http://lib.stat.cmu.edu/datasets/boston", seed=42):
    # Load the dataset
    df = pd.read_csv(data_url)

    # Set the random seed for reproducibility
    np.random.seed(seed)

    # Create a correlation matrix
    corr = df.corr()

    # Generate a heatmap using Seaborn
    ax = sns.heatmap(corr, annot=True, cmap="viridis")

    # Save the plot to a file
    fig = ax.get_figure()
    fig.savefig("heatmap.png")

    # Return the Axes object
    return ax