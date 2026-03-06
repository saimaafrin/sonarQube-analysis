
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def task_func(myList):
    # Create a MinMaxScaler object
    scaler = MinMaxScaler()

    # Fit the scaler to the data
    scaler.fit(myList)

    # Transform the data
    normalized_data = scaler.transform(myList)

    # Convert the normalized data to a numpy array
    normalized_array = np.array(normalized_data)

    return normalized_array