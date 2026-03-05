import pandas as pd
import random
N_DATA_POINTS = 10000
MIN_VALUE = 0.0
MAX_VALUE = 10.0
def task_func(n_data_points=N_DATA_POINTS):
    """
    Generate a random set of floating-point numbers, truncate each value to 3 decimal places, and return them in a DataFrame.
    The number of data points to generate can be specified. If zero, returns an empty DataFrame.
    """
    if n_data_points == 0:
        return pd.DataFrame()
    else:
        data = [round(random.uniform(MIN_VALUE, MAX_VALUE), 3) for _ in range(n_data_points)]
        return pd.DataFrame({'Value': data})