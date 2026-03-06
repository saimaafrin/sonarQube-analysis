
import numpy as np
import itertools

def task_func(data_list):
    # Check if the input list is empty
    if not data_list:
        return [], []

    # Unzip the list of tuples
    unzipped_list = list(itertools.zip_longest(*data_list, fillvalue=0))

    # Calculate the mean of the numeric values for each position
    mean_list = []
    for i, values in enumerate(unzipped_list):
        numeric_values = [value for value in values if isinstance(value, (int, float))]
        if numeric_values:
            mean = np.mean(numeric_values)
        else:
            mean = np.nan
        mean_list.append(mean)

    return mean_list, unzipped_list

mean_list, unzipped_list = task_func(data_list)
print(mean_list)
print(unzipped_list)