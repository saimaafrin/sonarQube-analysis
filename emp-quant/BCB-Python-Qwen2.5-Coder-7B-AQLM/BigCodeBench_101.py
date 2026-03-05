
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def task_func(data_url="http://lib.stat.cmu.edu/datasets/boston", seed=42):
    try:
        # Load the Boston Housing dataset
        boston = pd.read_csv(data_url, sep="\s+", header=None)
        boston.columns = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]
        
        # Calculate the correlation matrix
        corr_matrix = boston.corr()
        
        # Create a heatmap
        plt.figure(figsize=(10, 8))
        heatmap = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        
        # Set the title
        heatmap.set_title('Correlation Heatmap of Boston Housing Dataset')
        
        # Save the plot to a specified file if provided
        if 'save_file' in locals() and save_file:
            plt.savefig(save_file)
        
        # Show the plot
        plt.show()
        
        return heatmap
    except Exception as e:
        raise ValueError(f"An error occurred: {e}")