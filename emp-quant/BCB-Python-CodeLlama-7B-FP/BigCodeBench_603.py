import numpy as np
import pandas as pd
def task_func(matrix1, matrix2):
    """
    Connects two 2D numeric arrays (matrices) along the second axis (columns), converts them into a Pandas DataFrame, and returns a string representation of the DataFrame.
    """
    # Concatenate the two matrices along the second axis
    concatenated_matrix = np.concatenate((matrix1, matrix2), axis=1)

    # Convert the concatenated matrix into a Pandas DataFrame
    df = pd.DataFrame(concatenated_matrix)

    # Remove the index and header from the DataFrame
    df = df.drop(columns=['index'])
    df = df.drop(columns=['header'])

    # Return the string representation of the DataFrame
    return df.to_string(index=False, header=False)
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])