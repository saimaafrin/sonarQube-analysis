import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(P, T):
    """
    Perform matrix-tensor multiplication between a matrix P and a 3D tensor T,
    normalize the resulting 2D array, and return as a pandas DataFrame.
    
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
    result = np.einsum('ij, jkl -> ikl', P, T)
    
    # Flatten the result and normalize
    flattened_result = result.flatten()
    scaler = StandardScaler()
    normalized_result = scaler.fit_transform(flattened_result.reshape(-1, 1)).flatten()
    
    # Create DataFrame with normalized results
    df = pd.DataFrame(normalized_result, columns=['feature_' + str(i) for i in range(normalized_result.shape[0])])
    
    return df
P = np.array([[1, 2], [3, 4]])
T = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])