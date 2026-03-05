import pandas as pd
import seaborn as sns
import numpy as np
def task_func(array):
    # Check if the input array is empty
    if not array or not array[0]:
        raise ValueError("Input array is empty")
    
    # Check if all sublists have the same length
    if not all(len(sublist) == 5 for sublist in array):
        raise ValueError("Sublists have varying lengths")
    
    # Construct DataFrame from the input 2D list
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])
    
    # Calculate the correlation matrix
    correlation_matrix = df.corr()
    
    # Create a heatmap of the correlation matrix
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    
    return df, correlation_matrix
array = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6],
    [6, 5, 4, 3, 2],
    [3, 4, 5, 6, 7]
]