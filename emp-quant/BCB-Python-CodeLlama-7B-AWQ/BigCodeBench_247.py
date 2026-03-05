import pandas as pd
import random
from sklearn.preprocessing import StandardScaler
def task_func(n_data_points=5000, min_value=0.0, max_value=10.0):
    """
    Generate a random dataset of floating point numbers, truncate each value to 3 decimal places and normalize the data using standard scaling (mean = 0, std = 1).
    """
    if max_value < min_value:
        raise ValueError("max_value must be greater than min_value")

    # Generate random data
    data = [random.uniform(min_value, max_value) for _ in range(n_data_points)]

    # Truncate to 3 decimal places
    data = [round(x, 3) for x in data]

    # Normalize data using standard scaling
    scaler = StandardScaler()
    data = scaler.fit_transform(data)

    # Create DataFrame
    df = pd.DataFrame(data, columns=["Normalized Value"])

    return df