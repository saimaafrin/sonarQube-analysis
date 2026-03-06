
import numpy as np
import pandas as pd

# Constants
RANGE = (1, 100)

def task_func(L):
    """
    Generates a DataFrame filled with random integers based on the dimensions specified by pairs of integers in the input list of lists 'L'.

    Parameters:
    L (list of list of int): A list of lists where each inner list contains two integers representing the number of rows and columns for the DataFrame.

    Returns:
    pandas.DataFrame: A DataFrame with random integers.
    """
    # Initialize an empty list to store DataFrames
    dataframes = []
    
    # Iterate over each pair of integers in the input list of lists
    for row_count, col_count in L:
        # Generate a DataFrame with random integers
        df = pd.DataFrame(np.random.randint(RANGE[0], RANGE[1], size=(row_count, col_count)))
        # Append the DataFrame to the list
        dataframes.append(df)
    
    # Concatenate all DataFrames into a single DataFrame
    result_df = pd.concat(dataframes, ignore_index=True)
    
    return result_df