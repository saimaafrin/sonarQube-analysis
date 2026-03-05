import pandas as pd
import numpy as np
def task_func(rows=100, columns=3):
    """
    Generates a pandas DataFrame with random alphabets in each cell.
    
    Parameters:
    rows (int): The number of rows in the DataFrame.
    columns (int): The number of columns in the DataFrame.
    
    Returns:
    DataFrame: A pandas DataFrame with random alphabets.
    """
    # Generate random alphabets
    random_alphabets = np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), size=(rows, columns))
    
    # Create DataFrame
    df = pd.DataFrame(random_alphabets, columns=[chr(i) for i in range(97, 97 + columns)])
    
    return df