
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def task_func(data):
    # Check if the input data is a 2D array
    if not isinstance(data, np.ndarray) or len(data.shape) != 2:
        raise ValueError("Input data must be a 2D array.")
    
    # Convert the numpy array to a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Check if all columns contain numeric data
    if not np.issubdtype(df.values.dtype, np.number):
        raise ValueError("All columns in the input data must contain numeric data.")
    
    # Calculate the average of values across each row
    df['Average'] = df.mean(axis=1)
    
    # Calculate the correlation matrix
    corr_matrix = df.corr()
    
    # Create a heatmap of the correlation matrix
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
    
    return df, ax