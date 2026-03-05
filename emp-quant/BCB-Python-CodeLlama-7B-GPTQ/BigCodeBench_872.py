import numpy as np
import itertools
def task_func(data_list):
    """
    Unzips a list of tuples and calculates the mean of the numeric values for each position.
    The function accepts a list of tuples, where each tuple consists of alphanumeric values.
    It unzips the tuples, and calculates the mean of numeric values at each position using numpy,
    where non numeric values are ignored. If all values at a position are non numeric, the mean at this position is set to be np.nan.
    If the provided tuples have different number of entries, missing values are treated as zeros.
    The function should output with:
        list: A list of mean values for each numeric position across the tuples. Non-numeric positions are ignored.
        An empty list is returned if the input list (data_list) is empty.
    """
    # Check if the input list is empty
    if not data_list:
        return []

    # Unzip the tuples and convert them to a list of lists
    data_list = list(itertools.chain.from_iterable(data_list))

    # Calculate the mean of numeric values at each position using numpy
    means = np.nanmean(data_list, axis=0)

    # Replace np.nan with np.nanmean for non-numeric positions
    means[np.isnan(means)] = np.nanmean(means[np.isnan(means)])

    return means
data_list = [
    ('a', 1, 2, 3),
    ('b', 4, 5, 6),
    ('c', 7, 8, 9),
    ('d', 10, 11, 12),
]