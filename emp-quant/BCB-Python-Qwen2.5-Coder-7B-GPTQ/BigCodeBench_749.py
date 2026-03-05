from sklearn.preprocessing import MinMaxScaler
import numpy as np
def task_func(myList):
    """
    Normalize a list of numeric values to the range [0, 1] using min-max scaling.
    
    Parameters:
    myList (list): A list of numeric values to be normalized.
    
    Returns:
    ndarray: An array of normalized values.
    """
    # Convert the list to a numpy array
    data = np.array(myList)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Reshape the data to fit the scaler
    reshaped_data = data.reshape(-1, 1)
    
    # Perform min-max scaling
    normalized_data = scaler.fit_transform(reshaped_data)
    
    # Return the normalized data as a numpy array
    return normalized_data.flatten()
myList = [10, 20, 30, 40, 50]