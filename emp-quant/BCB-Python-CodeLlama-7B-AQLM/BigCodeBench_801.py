import collections
import numpy as np
def task_func(file_name):
    """
    Find the most common value in each column of a csv file with column names.

    If some values occur the same number of times, the values are sorted
    alphabetically and the first is considered most common.

    If an empty csv is passed, an empty dictionary is returned. 
    
    Parameters:
    file_name (str): The name of the csv file.
    
    Returns:
    dict: A dictionary with column names as keys and most common values as values.

    Requirements:
    - collections
    - numpy
    
    Example:
    >>> common_values = task_func('sample.csv')
    >>> print(common_values)
    {'Name': 'Simon Velasquez',
    'Age': 21,
    'Fruit': 'Apple',
    'Genre': 'HipHop',
    'Height': 172}
    """
    # Read the csv file
    data = np.genfromtxt(file_name, delimiter=',', dtype=str)

    # Get the column names
    column_names = data[0]

    # Remove the column names from the data
    data = data[1:]

    # Create an empty dictionary
    common_values = {}

    # Iterate over the columns
    for column in range(len(data[0])):
        # Get the column values
        column_values = [row[column] for row in data]

        # Get the most common value
        most_common_value = max(set(column_values), key=column_values.count)

        # Add the column name and most common value to the dictionary
        common_values[column_names[column]] = most_common_value

    return common_values