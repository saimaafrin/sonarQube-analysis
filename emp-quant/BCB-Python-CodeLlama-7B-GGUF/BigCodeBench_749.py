
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def normalize_list(myList):
    """
    Normalize a list of numeric values to the range [0, 1] using min-max scaling.

    Parameters
    ----------
    myList : list
        A list of numeric values to be normalized.

    Returns
    -------
    ndarray
        An array of normalized values.
    """
    scaler = MinMaxScaler()
    scaled_list = scaler.fit_transform(np.array(myList).reshape(-1, 1))
    return scaled_list