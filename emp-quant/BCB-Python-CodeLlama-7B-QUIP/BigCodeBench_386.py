
import numpy as np
import pandas as pd

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(length, min_value = 0, max_value = 100):
    # Generate random data
    data = np.random.rand(length, len(COLUMNS))
    # Calculate CDF
    cdf = np.cumsum(data, axis=1)
    # Create DataFrame
    df = pd.DataFrame(cdf, columns=COLUMNS)
    return df