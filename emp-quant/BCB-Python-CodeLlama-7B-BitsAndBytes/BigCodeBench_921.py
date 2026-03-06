
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(data, columns):
    # Create a MinMaxScaler object
    scaler = MinMaxScaler()

    # Fit the scaler to the data
    scaler.fit(data[columns])

    # Transform the data using the scaler
    scaled_data = scaler.transform(data[columns])

    # Create a new DataFrame with the scaled data
    scaled_df = pd.DataFrame(scaled_data, columns=columns)

    return scaled_df