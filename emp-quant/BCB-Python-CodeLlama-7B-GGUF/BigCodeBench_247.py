
import pandas as pd
import random
from sklearn.preprocessing import StandardScaler
# Constants
N_DATA_POINTS = 5000
MIN_VALUE = 0.0
MAX_VALUE = 10.0
def task_func(n_data_points=5000, min_value=0.0, max_value=10.0):
    if max_value < min_value:
        raise ValueError("max_value must be greater than or equal to min_value")
    data = pd.DataFrame(random.uniform(min_value, max_value, size=(n_data_points, 1)))
    scaler = StandardScaler()
    data["Normalized Value"] = scaler.fit_transform(data.iloc[:, 0].values.reshape(-1, 1))
    return data