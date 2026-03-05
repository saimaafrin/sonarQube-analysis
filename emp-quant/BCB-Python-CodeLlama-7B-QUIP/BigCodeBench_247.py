
import pandas as pd
import random
from sklearn.preprocessing import StandardScaler
# Constants
N_DATA_POINTS = 5000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def task_func(n_data_points=5000, min_value=0.0, max_value=10.0):
    # Generate random data
    data = random.uniform(min_value, max_value, size=(n_data_points, 1))
    # Truncate to 3 decimal places
    data = data.round(3)
    # Normalize using standard scaling
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Normalized Value'])
    return df