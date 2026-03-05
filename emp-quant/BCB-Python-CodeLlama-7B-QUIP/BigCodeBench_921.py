
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(data, columns):
    # Initialize the MinMaxScaler object
    scaler = MinMaxScaler()

    # Normalize the specified columns
    data[columns] = scaler.fit_transform(data[columns])

    # Return the normalized DataFrame
    return data