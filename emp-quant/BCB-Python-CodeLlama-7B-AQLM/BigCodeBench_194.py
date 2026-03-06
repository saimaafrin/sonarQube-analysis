import numpy as np
import matplotlib.pyplot as plt
BAR_COLOR = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']
def task_func(data_size):
    """
    Generates random numeric data and creates a histogram of the data.
    The color of the histogram bars is randomly selected from a predefined list.

    Parameters:
    data_size (int): The number of data points to generate.

    Returns:
    tuple:
        - ndarray: The array of randomly generated data.
        - str: The color used for the histogram bars.

    Requirements:
    - numpy
    - matplotlib

    Example:
    >>> data, color = task_func(5)
    >>> print(data.shape)
    (5,)
    >>> print(color in ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black'])
    True
    """
    data = np.random.randint(0, 10, data_size)
    color = np.random.choice(BAR_COLOR)
    return data, color