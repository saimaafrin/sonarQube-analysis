
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
    if P.shape[1] != T.shape[2]:
        raise ValueError("The number of columns in P must match the number of rows in T.")
    
    # Perform matrix-tensor multiplication
    result = np.einsum('ij,klj->kil', P, T)
    
    # Flatten the result to 2D for normalization
    flattened_result = result.reshape(result.shape[0], -1)
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the flattened result
    normalized_result = scaler.fit_transform(flattened_result)
    
    # Create a DataFrame with appropriate column names
    columns = [f'feature_{i}' for i in range(normalized_result.shape[1])]
    df = pd.DataFrame(normalized_result, columns=columns)
    
    return df