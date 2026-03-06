
import pandas as pd
import random
from sklearn.preprocessing import StandardScaler

# Constants
N_DATA_POINTS = 5000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def task_func(n_data_points=N_DATA_POINTS, min_value=MIN_VALUE, max_value=MAX_VALUE):
    # Generate random data
    data = [random.uniform(min_value, max_value) for _ in range(n_data_points)]

    # Truncate to 3 decimal places
    data = [round(x, 3) for x in data]

    # Normalize data using standard scaling
    scaler = StandardScaler()
    data = scaler.fit_transform(data)

    # Create a DataFrame with the normalized data
    df = pd.DataFrame(data, columns=['Normalized Value'])

    return df