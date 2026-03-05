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
    
    # Fit the scaler to the data and transform it
    normalized_data = scaler.fit_transform(data.reshape(-1, 1))
    
    return normalized_data.flatten()
myList = [10, 20, 30, 40, 50]