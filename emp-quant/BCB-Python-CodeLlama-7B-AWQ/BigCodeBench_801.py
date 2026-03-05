import collections
import numpy as np
def task_func(file_name):
    """
    Find the most common value in each column of a csv file with column names.
    If some values occur the same number of times, the values are sorted alphabetically and the first is considered most common.
    If an empty csv is passed, an empty dictionary is returned.
    """
    # Read the csv file
    data = np.genfromtxt(file_name, delimiter=',')

    # Create a dictionary to store the results
    results = {}

    # Iterate over each column of the data
    for i in range(data.shape[1]):
        # Get the unique values in the current column
        unique_values = np.unique(data[:, i])

        # If there are no unique values, skip this column
        if len(unique_values) == 0:
            continue

        # Get the counts of each value in the current column
        counts = np.bincount(data[:, i])

        # Find the most common value
        most_common_value = unique_values[np.argmax(counts)]

        # Add the result to the dictionary
        results[data.dtype.names[i]] = most_common_value

    return results
file_name = 'example.csv'