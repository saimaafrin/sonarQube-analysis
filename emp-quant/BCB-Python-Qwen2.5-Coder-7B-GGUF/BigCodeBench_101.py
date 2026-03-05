
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def task_func(data_url="http://lib.stat.cmu.edu/datasets/boston", seed=42):
    """
    Draws the correlation heatmap of the Boston Housing dataset using Seaborn.
    
    Parameters:
    - data_url: str, the URL of the Boston Housing dataset.
    - seed: int, the random seed for reproducibility.
    
    Returns:
    - matplotlib.axes.Axes: The Axes object containing the heatmap plot.
    
    Raises:
    - ValueError: If an error occurs in generating or saving the plot.
    """
    # Load the Boston Housing dataset
    boston = pd.read_csv(data_url, sep="\s+", header=None)
    boston.columns = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]
    
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Calculate the correlation matrix
    corr_matrix = boston.corr()
    
    # Create a heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    
    # Return the Axes object
    return ax