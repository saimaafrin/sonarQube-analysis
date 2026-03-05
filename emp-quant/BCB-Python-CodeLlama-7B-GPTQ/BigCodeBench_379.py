import pandas as pd
import numpy as np
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
def task_func(length):
    """
    Generate a Pandas DataFrame with specified length and random data and then record the data.
    """
    # Generate random data
    data = np.random.randint(0, 100, size=(length, len(COLUMNS)))
    # Create a Pandas DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)
    # Record the data
    df.to_csv('data.csv', index=False)
    return df