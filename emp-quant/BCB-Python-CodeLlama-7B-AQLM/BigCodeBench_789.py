import numpy as np
from sklearn.preprocessing import MinMaxScaler
ARRAY_LENGTH = 10
def task_func():
    """
    Generate a random array and apply min-max normalization (scaling) to transform the array values into a range between 0 and 1.

    Parameters:
    - None

    Returns:
    - scaled_array (numpy.ndarray): The normalized array.

    Requirements:
    - numpy
    - sklearn

    Example:
    >>> task_func()
    array([[0.57142857],
           [0.14285714],
           [0.71428571],
           [0.28571429],
           [0.57142857],
           [1.        ],
           [0.        ],
           [0.57142857],
           [0.71428571],
           [0.28571429]])
    """

    # Generate a random array
    array = np.random.rand(ARRAY_LENGTH)

    # Apply min-max normalization (scaling) to transform the array values into a range between 0 and 1
    scaler = MinMaxScaler()
    scaled_array = scaler.fit_transform(array.reshape(-1, 1))

    return scaled_array