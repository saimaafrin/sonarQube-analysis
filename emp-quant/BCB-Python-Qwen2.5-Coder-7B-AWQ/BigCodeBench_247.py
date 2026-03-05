import pandas as pd
import random
from sklearn.preprocessing import StandardScaler
N_DATA_POINTS = 5000
MIN_VALUE = 0.0
MAX_VALUE = 10.0
def task_func(n_data_points=N_DATA_POINTS, min_value=MIN_VALUE, max_value=MAX_VALUE):
    """
    Generates a random dataset of floating point numbers, truncates each value to 3 decimal places,
    and normalizes the data using standard scaling (mean = 0, std = 1).
    
    Parameters:
    n_data_points (int): The number of data points to generate.
    min_value (float): The minimum value for the random numbers.
    max_value (float): The maximum value for the random numbers.
    
    Returns:
    DataFrame: A pandas DataFrame with the normalized data.
    
    Raises:
    ValueError: If max_value is less than min_value.
    """
    if max_value < min_value:
        raise ValueError("max_value must be greater than or equal to min_value")
    
    # Generate random data
    data = [round(random.uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Original Value'])
    
    # Normalize the data
    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(df[['Original Value']])
    
    # Add the normalized data to the DataFrame
    df['Normalized Value'] = normalized_data
    
    return df