import pandas as pd
import numpy as np
def task_func(rows=100, columns=3):
    """
    Generates a pandas DataFrame with random alphabets.

    Parameters:
    rows (int): The number of rows in the DataFrame.
    columns (int): The number of columns in the DataFrame.

    Returns:
    DataFrame: A pandas DataFrame with random alphabets.
    """
    # Create a list of column names based on the number of columns
    columns = [chr(97 + i) for i in range(columns)]
    
    # Generate random alphabets for each cell
    data = np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), size=(rows, columns))
    
    # Create the DataFrame
    df = pd.DataFrame(data, columns=columns)
    
    return df