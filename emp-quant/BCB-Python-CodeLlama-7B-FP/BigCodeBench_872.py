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

    # Unzip the tuples
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=0))

    # Calculate the mean of numeric values at each position
    numeric_positions = [i for i, x in enumerate(unzipped_data) if np.issubdtype(type(x), np.number)]
    mean_values = [np.nanmean(x) for x in unzipped_data[numeric_positions]]

    # Return the list of mean values
    return mean_values
data_list = [
    ("apple", 10, 20),
    ("banana", 20, 30),
    ("orange", 30, 40),
    ("grape", 40, 50),
]