
import pandas as pd
import seaborn as sns
import numpy as np

def task_func(array):
    if not array or any(len(sublist) != 5 for sublist in array):
        raise ValueError("Input array must not be empty and must contain sublists of length 5.")
    
    # Convert the 2D list to a pandas DataFrame
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])
    
    # Calculate the correlation matrix
    correlation_matrix = df.corr()
    
    # Create a heatmap of the correlation matrix
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    
    return df, heatmap