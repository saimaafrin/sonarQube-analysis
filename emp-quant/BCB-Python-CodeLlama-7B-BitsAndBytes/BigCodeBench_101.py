
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def task_func(data_url="http://lib.stat.cmu.edu/datasets/boston", seed=42):
    # Load the Boston Housing dataset
    data = pd.read_csv(data_url)

    # Create a correlation matrix
    corr = data.corr()

    # Generate a heatmap
    sns.heatmap(corr, annot=True, cmap="coolwarm")

    # Save the heatmap to a file
    plt.savefig("heatmap.png")

    # Return the Axes object containing the heatmap plot
    return plt.gca()

# Call the function and save the heatmap to a file
try:
    task_func(data_url="http://lib.stat.cmu.edu/datasets/boston", seed=42)
except ValueError as e:
    print(f"ValueError: {e}")