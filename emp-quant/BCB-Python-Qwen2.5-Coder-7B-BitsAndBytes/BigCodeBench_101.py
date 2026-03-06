
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def task_func(data_url="http://lib.stat.cmu.edu/datasets/boston", seed=42):
    try:
        # Load the Boston Housing dataset
        boston = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
        boston.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
        
        # Calculate the correlation matrix
        corr_matrix = boston.corr()
        
        # Create a figure and axis for the heatmap
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Draw the correlation heatmap
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
        
        # Set the title of the plot
        ax.set_title('Correlation Heatmap of Boston Housing Dataset')
        
        # Return the Axes object
        return ax
    
    except Exception as e:
        raise ValueError(f"An error occurred: {e}")