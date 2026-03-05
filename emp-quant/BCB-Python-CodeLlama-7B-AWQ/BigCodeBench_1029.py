import pandas as pd
import numpy as np
def task_func(rows=100, columns=3):
    """
    Create a Pandas DataFrame with random alphabets in each cell.
    The DataFrame will have a specified number of rows and columns.
    Each column is named with a string from the list ['a', 'b', 'c', ...] depending on the number of columns specified.
    """
    # Create a list of random alphabets
    alphabets = [chr(ord('a') + i) for i in range(columns)]

    # Create a DataFrame with the random alphabets
    df = pd.DataFrame(np.random.randint(0, 26, size=(rows, columns)), columns=alphabets)

    return df
rows = 10
columns = 5