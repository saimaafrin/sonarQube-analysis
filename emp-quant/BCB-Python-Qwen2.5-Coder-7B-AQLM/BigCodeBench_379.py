
import pandas as pd
import numpy as np

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(length):
    """
    Generates a Pandas DataFrame with specified length and random data.

    Parameters:
    length (int): The number of rows in the DataFrame.

    Returns:
    DataFrame: A pandas DataFrame with random data.
    """
    # Generate random data
    data = np.random.rand(length, len(COLUMNS))
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)
    
    return df