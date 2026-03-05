import pandas as pd
import seaborn as sns
import numpy as np
def task_func(array):
    # Check if the input array is empty
    if not array:
        raise ValueError("Input array is empty")
    
    # Check if all sublists have the same length
    if not all(len(sublist) == 5 for sublist in array):
        raise ValueError("All sublists must have the same length of 5")
    
    # Create a DataFrame from the input 2D list
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])
    
    # Calculate the correlation matrix
    correlation_matrix = df.corr()
    
    # Create a heatmap of the correlation matrix
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    
    return df, heatmap