
import numpy as np
import itertools

def task_func(data_list):
    # Check if the input list is empty
    if not data_list:
        return []

    # Unzip the tuples and convert to a list of lists
    data_list = list(itertools.chain.from_iterable(data_list))

    # Calculate the mean of numeric values at each position
    means = []
    for i, val in enumerate(data_list):
        if np.issubdtype(type(val), np.number):
            means.append(np.nanmean(val))
        else:
            means.append(np.nan)

    return means