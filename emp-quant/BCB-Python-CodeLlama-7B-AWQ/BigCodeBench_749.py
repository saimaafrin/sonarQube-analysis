from sklearn.preprocessing import MinMaxScaler
import numpy as np
def task_func(myList):
    """
    Normalize a list of numeric values to the range [0, 1] using min-max scaling.

    Args:
        myList (list): A list of numeric values.

    Returns:
        ndarray: An array of normalized values.
    """
    scaler = MinMaxScaler()
    return scaler.fit_transform(np.array(myList).reshape(-1, 1))
myList = [1, 2, 3, 4, 5]