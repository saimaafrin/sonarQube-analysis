
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(P, T):
    # Check if the shapes of P and T are compatible for multiplication
    if P.shape[1] != T.shape[0]:
        raise ValueError("Shapes of P and T are not compatible for multiplication")

    # Perform matrix-tensor multiplication
    result = np.matmul(P, T)

    # Normalize the result using StandardScaler
    scaler = StandardScaler()
    result = scaler.fit_transform(result.reshape(-1, 1))

    # Return the normalized result as a pandas DataFrame
    return pd.DataFrame(result, columns=["feature_%d" % i for i in range(result.shape[1])])