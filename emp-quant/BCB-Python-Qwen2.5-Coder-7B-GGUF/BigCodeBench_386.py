
import numpy as np
import pandas as pd

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(length, min_value=0, max_value=100):
    # Generate random data for the DataFrame
    data = {col: np.random.uniform(min_value, max_value, length) for col in COLUMNS}
    df = pd.DataFrame(data)
    
    # Calculate the cumulative distribution function (CDF)
    cdf = df.cumsum() / df.sum()
    
    return df, cdf