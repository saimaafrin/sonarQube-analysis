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
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Load the Boston Housing dataset
    boston_data = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
    boston_data.columns = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]
    
    # Calculate the correlation matrix
    correlation_matrix = boston_data.corr()
    
    # Create a heatmap
    try:
        plt.figure(figsize=(10, 8))
        heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Heatmap of Boston Housing Dataset')
        plt.show()
        return heatmap
    except Exception as e:
        raise ValueError(f"An error occurred: {e}")