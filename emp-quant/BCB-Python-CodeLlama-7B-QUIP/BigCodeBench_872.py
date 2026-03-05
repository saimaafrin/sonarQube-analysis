
import numpy as np
import itertools

def task_func(data_list):
    # Check if the input list is empty
    if len(data_list) == 0:
        return []

    # Unzip the tuples
    data = [list(x) for x in data_list]

    # Calculate the mean of numeric values at each position using numpy
    means = [np.nanmean(x) for x in data]

    # Ignore non-numeric values
    means = [x[x != ''] for x in means]

    # Set the mean to np.nan if all values at a position are non-numeric
    means = [np.nan if x == [] else x for x in means]

    return means