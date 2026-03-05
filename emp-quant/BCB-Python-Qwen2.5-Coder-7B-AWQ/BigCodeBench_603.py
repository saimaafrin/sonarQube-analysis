import numpy as np
import pandas as pd
def task_func(matrix1, matrix2):
    """
    Connects two 2D numeric arrays (matrices) along the second axis (columns),
    converts them into a Pandas DataFrame, and returns a string representation of the DataFrame.
    
    Parameters:
    matrix1 (np.ndarray): The first 2D numeric array.
    matrix2 (np.ndarray): The second 2D numeric array.
    
    Returns:
    str: The string representation of the DataFrame without the index and header.
    """
    # Concatenate the matrices along the second axis
    combined_matrix = np.hstack((matrix1, matrix2))
    
    # Convert the combined matrix to a DataFrame
    df = pd.DataFrame(combined_matrix)
    
    # Return the string representation of the DataFrame without the index and header
    return df.to_string(index=False, header=False)