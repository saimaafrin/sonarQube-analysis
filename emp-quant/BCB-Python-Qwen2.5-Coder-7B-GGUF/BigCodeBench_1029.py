
import pandas as pd
import numpy as np

def task_func(rows=100, columns=3):
    """
    Create a Pandas DataFrame with random alphabets in each cell.
    
    Parameters:
    rows (int): The number of rows in the DataFrame.
    columns (int): The number of columns in the DataFrame.
    
    Returns:
    DataFrame: A pandas DataFrame with random alphabets.
    """
    # Define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Create a DataFrame with random alphabets
    data = np.random.choice(list(alphabet), size=(rows, columns))
    df = pd.DataFrame(data, columns=[chr(97 + i) for i in range(columns)])
    
    return df