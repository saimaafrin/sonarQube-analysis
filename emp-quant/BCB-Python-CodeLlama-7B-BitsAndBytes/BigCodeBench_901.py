
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Updated function to handle empty input list
def task_func(d):
    if not d:
        return pd.DataFrame()

    # Create a MinMaxScaler object
    scaler = MinMaxScaler()

    # Scale the data
    scaled_data = scaler.fit_transform(d)

    # Create a DataFrame from the scaled data
    df = pd.DataFrame(scaled_data, columns=['x', 'y', 'z'])

    return df