import collections
import numpy as np
def task_func(file_name):
    """
    Find the most common value in each column of a csv file with column names.
    If some values occur the same number of times, the values are sorted alphabetically and the first is considered most common.
    If an empty csv is passed, an empty dictionary is returned.
    """
    # Read the csv file
    data = np.genfromtxt(file_name, delimiter=',', dtype=str)

    # Create a dictionary to store the most common values
    most_common_values = {}

    # Iterate over the columns of the csv file
    for i in range(data.shape[1]):
        # Get the values in the current column
        column_values = data[:, i]

        # Get the most common value in the current column
        most_common_value = collections.Counter(column_values).most_common(1)[0][0]

        # Add the most common value to the dictionary
        most_common_values[data.dtype.names[i]] = most_common_value

    # Return the dictionary with the most common values
    return most_common_values
file_name = 'example.csv'