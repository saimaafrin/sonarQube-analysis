
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(P, T):
    # Check if the shapes of P and T are compatible for multiplication
    if P.shape[1] != T.shape[0]:
        raise ValueError("Incompatible shapes for matrix P and tensor T")
    
    # Perform matrix-tensor multiplication
    result = np.dot(P, T)
    
    # Normalize the resulting 2D array using StandardScaler
    scaler = StandardScaler()
    normalized_result = scaler.fit_transform(result)
    
    # Convert the normalized result to a pandas DataFrame
    df = pd.DataFrame(normalized_result, columns=[f"feature_{i}" for i in range(normalized_result.shape[1])])
    
    return df