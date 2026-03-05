
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def task_func(myList):
    # Convert the list to a numpy array
    data = np.array(myList)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    normalized_data = scaler.fit_transform(data.reshape(-1, 1))
    
    # Return the normalized data as a numpy array
    return normalized_data