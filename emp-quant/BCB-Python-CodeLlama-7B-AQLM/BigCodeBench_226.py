import numpy as np
import math
import matplotlib.pyplot as plt
def task_func(range_start=0, range_end=10, step=0.1):
    """
    Create a generator object that generates a sequence of tuples.
    Each tuple contains x and e^x values. Plot the exponential function using these values.

    Returns:
    tuple: 
        - A generator object that yields tuples of (x, e^x).
        - The plotted Axes object of the exponential function.

    Requirements:
    - numpy
    - math
    - matplotlib.pyplot

    Example:
    >>> data, ax = task_func()
    >>> print(next(data))
    (0.0, 1.0)
    >>> ax.get_title()  # Returns the title of the plot
    'Exponential Function Plot'
    """
    # TODO: Implement the function
    # Hint: Use the following formula: e^x = 1 + x + x^2/2! + x^3/3! + ...
    # Hint: Use the following formula: x^n = x * x^(n-1)
    # Hint: Use the following formula: n! = n * (n-1) * ... * 1
    # Hint: Use the following formula: 1/n! = 1/1 * 1/2 * ... * 1/n
    # Hint: Use the following formula: 1/n! = 1 / (n * (n-1) * ... * 1)
    # Hint: Use the following formula: 1/n! = 1 / n! * 1 / (n-1) * ... * 1 / 1
    # Hint: Use the following formula: 1/n! = 1 / (n * (n-1) * ... * 1)
    # Hint: Use the following formula: 1/n! = 1 / n! * 1 / (n-1) * ... * 1 / 1
    # Hint: Use the following formula: 1/n! = 1 / (n * (n-1) * ... * 1)
    # Hint: Use the following formula: 1/n! = 1 / n! * 1 / (n-1) * ... * 1 / 1
    # Hint: Use the following formula: 1/n! = 1 / (n * (n-1) * ... * 1)
    # Hint: Use the following formula: 1/n! = 1 / n! * 1 / (n-1) * ... * 1 / 1
    # Hint: Use the following formula: 1/n! = 1 / (n * (n-1) * ... * 1)
    # Hint: Use the following formula: 1/n! = 1 / n! * 1 / (n-1) * ... * 1 / 1
    # Hint: Use the following formula: 1/n! = 1 / (n * (n-1) * ... * 1)
    # Hint: Use the following formula: 1/n! = 1 / n! * 1 / (n-1) * ... * 1 / 1
    # Hint: Use the following formula: 1/n! = 1 / (n * (n-1) * ... * 1)
    # Hint: Use the following formula: 1/n! = 1 / n! * 1 / (n-1) * ... * 1 / 1
    # Hint: Use the following formula: 1/n! = 1 / (n * (n-1) * ... * 1)
    # Hint: Use the following formula: 1/n! = 1 / n! * 1 / (n-1) * ... * 1 / 1
    # Hint: Use the following formula: 1/n! = 1 / (n * (n-1) * ... * 1)
    # Hint: Use the following formula: 1/n! = 1 / n! * 1 / (n-1) * ... * 1 / 1
    # Hint: Use the following formula: 1/n! = 1 / (n * (n-1) * ... * 1)
    # Hint: Use the following formula: 1/n! = 1 / n! * 1 / (n-1) * ... * 1 / 1
    # Hint: Use the following formula: 1/n! = 1 / (n * (n-1) * ... * 1)
    # Hint: Use the following formula: 1/n! = 1 / n! * 1 / (n-1) * ... * 1 / 1
    # Hint: Use the following formula: 1/n! = 1 / (n * (n-1) * ... * 1)
    # Hint: Use the following formula: 1/n! = 1 / n! * 1 / (n-1) * ... * 1 / 1
    # Hint: Use the following formula: 1/n! = 1 / (n * (n-1) * ... * 1)
    # Hint: Use the following formula: 1/n! = 1 / n! * 1 / (n-1) * ... * 1 / 1
    # Hint: Use the following formula: 1/n! = 1 / (n * (n-1) * ... * 1)
    # Hint: Use the following formula: 1/n! = 1 / n! * 1 / (n-1) * ... * 1 / 1
    # Hint: Use the following formula: 1/n! = 1 / (n * (n-1) * ... * 1)
    # Hint: Use the following formula: 1/n! = 1 / n! * 1 / (n-1) * ... * 1 / 1
    # Hint: Use the following formula: 1/n! = 1 / (n * (n-1) * ... * 1)
    # Hint: Use the following formula: 1/n! = 1 / n! * 1 /