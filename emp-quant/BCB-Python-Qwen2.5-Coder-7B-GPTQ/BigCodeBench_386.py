import numpy as np
import pandas as pd
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
def task_func(length, min_value=0, max_value=100):
    """
    Generates a pandas DataFrame with specified ranges and length, and calculates the cumulative distribution function (CDF).
    
    Parameters:
    - length: int, the number of rows in the DataFrame.
    - min_value: int, the minimum value for the random numbers.
    - max_value: int, the maximum value for the random numbers.
    
    Returns:
    - DataFrame: A pandas DataFrame with the calculated cumulative distribution function (CDF).
    """
    # Generate random data
    data = {col: np.random.uniform(min_value, max_value, length) for col in COLUMNS}
    df = pd.DataFrame(data)
    
    # Calculate CDF for each column
    cdf = df.apply(pd.Series.cumsum)
    
    return cdf
length = 10