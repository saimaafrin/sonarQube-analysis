
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(P, T):
    # Check if the shapes of P and T are compatible for multiplication
    if P.shape[1] != T.shape[0]:
        raise ValueError("Shapes of P and T are not compatible for multiplication")

    # Perform matrix-tensor multiplication
    result = np.matmul(P, T)

    # Flatten the result
    flattened_result = result.flatten()

    # Normalize the flattened result using StandardScaler
    scaler = StandardScaler()
    normalized_result = scaler.fit_transform(flattened_result)

    # Create a DataFrame with the normalized result
    df = pd.DataFrame(normalized_result, columns=["feature_%d" % i for i in range(normalized_result.shape[1])])

    return df