
import pandas as pd
import random
from sklearn.preprocessing import StandardScaler

# Constants
N_DATA_POINTS = 5000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def task_func(n_data_points=N_DATA_POINTS, min_value=MIN_VALUE, max_value=MAX_VALUE):
    if max_value < min_value:
        raise ValueError("max_value must be greater than or equal to min_value")
    
    # Generate random dataset
    data = [random.uniform(min_value, max_value) for _ in range(n_data_points)]
    
    # Truncate each value to 3 decimal places
    data = [round(x, 3) for x in data]
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Original Value'])
    
    # Normalize the data
    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(df)
    
    # Add 'Normalized Value' column to DataFrame
    df['Normalized Value'] = normalized_data
    
    return df