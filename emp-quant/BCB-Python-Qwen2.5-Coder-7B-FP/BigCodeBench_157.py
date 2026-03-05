import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
def task_func(data):
    # Check if the input data is a 2D array
    if not isinstance(data, np.ndarray) or len(data.shape) != 2:
        raise ValueError("Input data must be a 2D array.")
    
    # Check if the input data contains non-numeric data
    if not np.issubdtype(data.dtype, np.number):
        raise ValueError("Input data must contain only numeric values.")
    
    # Convert the numpy array to a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Calculate the average of values across each row
    df['Average'] = df.mean(axis=1)
    
    # Calculate the correlation matrix
    corr_matrix = df.corr()
    
    # Create a heatmap of the correlations
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
    
    return df, ax