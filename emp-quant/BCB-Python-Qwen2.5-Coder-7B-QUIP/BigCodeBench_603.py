
import numpy as np
import pandas as pd

def task_func(matrix1, matrix2):
    # Concatenate the matrices along the second axis
    concatenated_matrix = np.concatenate([matrix1, matrix2], axis=1)
    
    # Convert the concatenated matrix to a DataFrame
    df = pd.DataFrame(concatenated_matrix)
    
    # Return the string representation of the DataFrame without the index and header
    return df.to_string(index=False, header=False)