import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(P, T):
    """
    Perform matrix-tensor multiplication between a matrix P and a 3D tensor T,
    then return a dataframe of normalized results.
    
    Parameters:
    - P: A 2D numpy array representing the matrix.
    - T: A 3D numpy array representing the tensor.
    
    Returns:
    - pandas.DataFrame: A DataFrame with the normalized result.
    """
    # Check if the shapes are compatible for multiplication
    if P.shape[1] != T.shape[0]:
        raise ValueError("The number of columns in P must match the number of rows in T.")
    
    # Perform matrix-tensor multiplication
    result = np.dot(P, T)
    
    # Flatten the result to a 2D array
    flattened_result = result.reshape(-1, result.shape[-1])
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the flattened result
    normalized_result = scaler.fit_transform(flattened_result)
    
    # Create a DataFrame with the normalized result
    df = pd.DataFrame(normalized_result, columns=[f'feature_{i}' for i in range(normalized_result.shape[1])])
    
    return df
P = np.array([[1, 2], [3, 4]])
T = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])