
import collections
import numpy as np

def task_func(file_name):
    # Read the csv file
    data = np.genfromtxt(file_name, delimiter=',')

    # Get the column names
    column_names = data[0]

    # Create an empty dictionary to store the results
    results = {}

    # Iterate over the columns
    for i in range(1, len(data)):
        # Get the values in the current column
        column_values = data[i]

        # Find the most common value
        most_common_value = collections.Counter(column_values).most_common(1)[0][0]

        # Add the result to the dictionary
        results[column_names[i]] = most_common_value

    return results