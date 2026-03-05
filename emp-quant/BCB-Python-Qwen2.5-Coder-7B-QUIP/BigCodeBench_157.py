
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.utils import check_array

def task_func(data):
    # Check if the input data is a 2D array
    if not isinstance(data, np.ndarray) or len(data.shape) != 2:
        raise ValueError("Input data must be a 2D array")
    
    # Check if the input data contains only numeric values
    if not np.issubdtype(data.dtype, np.number):
        raise ValueError("Input data must contain only numeric values")
    
    # Calculate the average of values across each row
    data['Average'] = data.mean(axis=1)
    
    # Calculate the correlation matrix
    corr_matrix = data.corr()
    
    # Create a heatmap of the correlation matrix
    fig, ax = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
    
    # Return the DataFrame with the average column and the heatmap axes
    return data, ax