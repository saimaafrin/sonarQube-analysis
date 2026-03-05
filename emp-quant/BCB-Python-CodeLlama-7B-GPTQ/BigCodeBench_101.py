import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
def task_func(data_url="http://lib.stat.cmu.edu/datasets/boston", seed=42):
    """
    Draw the correlation heatmap of the Boston Housing dataset using Seaborn, with an option to save it to a specified file.
    """
    # Load the dataset
    data = pd.read_csv(data_url)

    # Generate the heatmap
    sns.heatmap(data.corr(), annot=True, cmap="coolwarm")

    # Save the plot to a file
    if save_file:
        plt.savefig(save_file)

    # Return the Axes object containing the heatmap plot
    return plt.gca()
data_url = "http://lib.stat.cmu.edu/datasets/boston"
save_file = "boston_heatmap.png"