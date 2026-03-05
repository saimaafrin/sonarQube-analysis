import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(P, T):
    """
    Calculate the product of matrix "P" and 3D tensor "T" then return dataframe of normalized results.
    This function performs matrix-tensor multiplication between a matrix "P" and a 3D tensor "T" using numpy.
    It checks if the shapes of P and T are compatible for multiplication, raising a ValueError if they are not.
    The function then normalizes the resulting 2D array using sklearn's StandardScaler.
    The final output is returned as a pandas DataFrame, with columns named feature_0, feature_1, ..., feature_n, where n is the number of features in the flattened result of the matrix-tensor multiplication.
    """
    # Check if the shapes of P and T are compatible for multiplication
    if P.shape[1] != T.shape[0]:
        raise ValueError("Shapes of P and T are not compatible for multiplication")

    # Perform matrix-tensor multiplication
    result = np.matmul(P, T)

    # Normalize the result using StandardScaler
    scaler = StandardScaler()
    result = scaler.fit_transform(result)

    # Convert result to a pandas DataFrame
    result = pd.DataFrame(result, columns=["feature_%d" % i for i in range(result.shape[1])])

    return result
P = np.array([[1, 2], [3, 4]])
T = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])