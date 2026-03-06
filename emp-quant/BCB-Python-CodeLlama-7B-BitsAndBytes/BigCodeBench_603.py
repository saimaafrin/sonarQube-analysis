
import numpy as np
import pandas as pd

def task_func(matrix1, matrix2):
    # Concatenate the two matrices along the second axis (columns)
    concatenated_matrix = np.concatenate((matrix1, matrix2), axis=1)

    # Convert the concatenated matrix to a Pandas DataFrame
    df = pd.DataFrame(concatenated_matrix)

    # Remove the index and header from the DataFrame
    df = df.reset_index(drop=True)
    df.columns = ['Column ' + str(i) for i in range(df.shape[1])]

    # Return the string representation of the DataFrame
    return df.to_string(index=False, header=False)