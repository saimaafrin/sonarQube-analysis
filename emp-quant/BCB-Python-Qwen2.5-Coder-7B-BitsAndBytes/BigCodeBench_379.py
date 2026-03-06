
import pandas as pd
import numpy as np

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(length):
    """
    Generates a pandas DataFrame with specified length and random data.

    Parameters:
    - length (int): The number of rows in the DataFrame.

    Returns:
    - DataFrame: A pandas DataFrame with random data.
    """
    # Create a dictionary to hold the data for each column
    data = {col: np.random.rand(length) for col in COLUMNS}
    
    # Create the DataFrame from the dictionary
    df = pd.DataFrame(data)
    
    return df