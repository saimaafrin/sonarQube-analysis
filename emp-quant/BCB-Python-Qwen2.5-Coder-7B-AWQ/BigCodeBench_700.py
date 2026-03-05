import pandas as pd
import numpy as np
def task_func(data, cols):
    """
    Convert the provided data into a DataFrame and calculate the correlation matrix of numeric columns.

    Parameters:
    data (list of lists): The data to be converted into a DataFrame.
    cols (list of str): The column names for the DataFrame.

    Returns:
    correlation_matrix (pd.DataFrame): The correlation matrix.
    """
    # Create a DataFrame from the provided data and columns
    df = pd.DataFrame(data, columns=cols)
    
    # Filter the DataFrame to include only numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Calculate the correlation matrix
    correlation_matrix = numeric_df.corr()
    
    return correlation_matrix