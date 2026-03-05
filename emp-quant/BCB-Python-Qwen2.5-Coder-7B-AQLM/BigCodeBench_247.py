
import pandas as pd
import random
from sklearn.preprocessing import StandardScaler

# Constants
N_DATA_POINTS = 5000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def task_func(n_data_points=5000, min_value=0.0, max_value=10.0):
    if max_value < min_value:
        raise ValueError("max_value must be greater than min_value")
    
    # Generate random dataset
    data = [random.uniform(min_value, max_value) for _ in range(n_data_points)]
    
    # Truncate each value to 3 decimal places
    data = [round(value, 3) for value in data]
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Original Value'])
    
    # Normalize the data
    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(df)
    
    # Create DataFrame with normalized data
    normalized_df = pd.DataFrame(normalized_data, columns=['Normalized Value'])
    
    return normalized_df