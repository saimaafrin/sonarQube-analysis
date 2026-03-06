
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def task_func(myList):
    # Convert the input list to a numpy array
    data = np.array(myList)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data to the range [0, 1]
    normalized_data = scaler.fit_transform(data.reshape(-1, 1))
    
    return normalized_data.flatten()