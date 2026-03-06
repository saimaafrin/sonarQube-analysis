
import numpy as np
from scipy.stats import iqr

def task_func(L):
    """
    Calculate the interquartile range of all elements in a nested list 'L'.

    Args:
        L (list): A nested list of numbers.

    Returns:
        iqr_value (float): The interquartile range.
    """
    # Calculate the interquartile range
    iqr_value = iqr(L)

    # Print the result
    print(f"The interquartile range is {iqr_value:.2f}")