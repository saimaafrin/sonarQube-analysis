import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
def task_func(data):
    # Check if the input data is a 2D array
    if not isinstance(data, np.ndarray) or len(data.shape) != 2:
        raise ValueError("Input data must be a 2D numpy array.")
    
    # Check if the input data contains only numeric values
    if not np.issubdtype(data.dtype, np.number):
        raise ValueError("Input data must contain only numeric values.")
    
    # Convert the numpy array to a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Calculate the average of values across each row
    df['Average'] = df.mean(axis=1)
    
    # Calculate the correlation matrix
    correlation_matrix = df.corr()
    
    # Create a heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    
    # Return the DataFrame and the Axes object
    return df, heatmap