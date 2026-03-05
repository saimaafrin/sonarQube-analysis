import collections
import numpy as np
def task_func(file_name):
    """
    Find the most common value in each column of a csv file with column names.
    If some values occur the same number of times, the values are sorted alphabetically and the first is considered most common.
    If an empty csv is passed, an empty dictionary is returned.
    :param file_name: The name of the csv file.
    :return: A dictionary with column names as keys and most common values as values.
    """
    # Read the csv file
    data = np.genfromtxt(file_name, delimiter=',')

    # Get the column names
    column_names = data[0]

    # Initialize an empty dictionary to store the results
    results = {}

    # Iterate over the columns
    for i in range(1, len(data)):
        # Get the values in the current column
        column_values = data[:, i]

        # Get the most common value in the column
        most_common_value = collections.Counter(column_values).most_common(1)[0][0]

        # Add the result to the dictionary
        results[column_names[i]] = most_common_value

    # Return the results
    return results
file_name = 'example.csv'