
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def task_func(data_url="http://lib.stat.cmu.edu/datasets/boston", seed=42):
    """
    Draw the correlation heatmap of the Boston Housing dataset using Seaborn, with an option to save it to a specified file.
    
    Parameters:
    data_url (str): The URL of the Boston Housing dataset.
    seed (int): The seed for the random number generator.
    
    Returns:
    matplotlib.axes.Axes: The Axes object containing the heatmap plot.
    
    Raises:
    ValueError: If an error occurs in generating or saving the plot.
    """
    # Load the Boston Housing dataset
    try:
        boston = pd.read_csv(data_url, sep='\t')
    except Exception as e:
        raise ValueError(f"Error loading dataset: {e}")
    
    # Calculate the correlation matrix
    corr_matrix = boston.corr()
    
    # Create the heatmap
    try:
        fig, ax = plt.subplots()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
        plt.title('Correlation Heatmap of Boston Housing Dataset')
        plt.show()
    except Exception as e:
        raise ValueError(f"Error creating heatmap: {e}")
    
    # Save the heatmap to a file
    try:
        plt.savefig('boston_heatmap.png')
    except Exception as e:
        raise ValueError(f"Error saving heatmap: {e}")
    
    return ax