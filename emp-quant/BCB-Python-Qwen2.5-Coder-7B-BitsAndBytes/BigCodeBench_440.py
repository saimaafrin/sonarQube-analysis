
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(P, T):
    """
    Perform matrix-tensor multiplication between a matrix 'P' and a 3D tensor 'T',
    normalize the resulting 2D array, and return it as a pandas DataFrame.

    Parameters:
    - P (np.ndarray): A 2D numpy array representing the matrix.
    - T (np.ndarray): A 3D numpy array representing the tensor.

    Returns:
    - pd.DataFrame: A DataFrame with the normalized result.
    """
    # Check if the shapes are compatible for multiplication
    if P.shape[1] != T.shape[0]:
        raise ValueError("Incompatible dimensions for matrix and tensor multiplication.")
    
    # Perform matrix-tensor multiplication
    result = np.dot(P, T)
    
    # Flatten the result to perform normalization
    flattened_result = result.flatten()
    
    # Initialize the scaler
    scaler = StandardScaler()
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(flattened_result.reshape(-1, 1))
    
    # Create a DataFrame with the scaled data
    df = pd.DataFrame(scaled_data, columns=[f'feature_{i}' for i in range(scaled_data.shape[1])])
    
    return df