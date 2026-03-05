import pandas as pd
import random
N_DATA_POINTS = 10000
MIN_VALUE = 0.0
MAX_VALUE = 10.0
def task_func(n_data_points=N_DATA_POINTS):
    """
    Generate a random set of floating-point numbers, truncate each value to 3 decimal places,
    and return them in a DataFrame. The number of data points to generate can be specified.
    If zero, returns an empty DataFrame.
    
    Parameters:
    n_data_points (int): The number of data points to generate. Defaults to N_DATA_POINTS.
    
    Returns:
    DataFrame: A pandas DataFrame containing one column 'Value' with the generated data. Empty if n_data_points is 0.
    """
    if n_data_points == 0:
        return pd.DataFrame(columns=['Value'])
    
    # Generate random floating-point numbers
    random_floats = [random.uniform(MIN_VALUE, MAX_VALUE) for _ in range(n_data_points)]
    
    # Truncate each value to 3 decimal places
    truncated_floats = [round(num, 3) for num in random_floats]
    
    # Create DataFrame
    df = pd.DataFrame(truncated_floats, columns=['Value'])
    
    return df