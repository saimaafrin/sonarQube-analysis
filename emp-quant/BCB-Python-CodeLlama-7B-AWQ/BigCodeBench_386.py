import numpy as np
import pandas as pd
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
def task_func(length, min_value = 0, max_value = 100):
    """
    Generate a pandas DataFrame with specified ranges and length, and calculate the cumulative distribution function (CDF).
    """
    # Generate random data
    data = np.random.randint(min_value, max_value, size=(length, len(COLUMNS)))

    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=COLUMNS)

    # Calculate the CDF
    cdf = df.cumsum()

    # Return the DataFrame with the CDF
    return cdf