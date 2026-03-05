
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def task_func(data_url="http://lib.stat.cmu.edu/datasets/boston", seed=42):
    # Load the Boston Housing dataset
    df = pd.read_csv(data_url)

    # Generate the correlation heatmap
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")

    # Save the plot to a file
    plt.savefig("correlation_heatmap.png")

    # Return the Axes object containing the heatmap plot
    return plt.gca()