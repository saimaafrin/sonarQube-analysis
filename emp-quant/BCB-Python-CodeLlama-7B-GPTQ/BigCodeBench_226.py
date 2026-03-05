import numpy as np
import math
import matplotlib.pyplot as plt
def task_func(range_start=0, range_end=10, step=0.1):
    """
    Generates a sequence of tuples containing x and e^x values.
    """
    x = np.arange(range_start, range_end, step)
    y = np.exp(x)
    return zip(x, y)