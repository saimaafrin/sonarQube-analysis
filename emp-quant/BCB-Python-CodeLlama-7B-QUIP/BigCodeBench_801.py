
import collections
import numpy as np

def task_func(file_name):
    # Open the file and read it into a list of lists
    with open(file_name, 'r') as f:
        data = f.read().split('\n')

    # Create an empty dictionary to store the column names and their most common values
    column_dict = collections.defaultdict(list)

    # Iterate over the rows of the file and find the most common value in each column
    for row in data:
        for i, value in enumerate(row.split(',')):
            column_dict[i].append(value)

    # Sort the values in each column alphabetically and take the first one as the most common value
    for column in column_dict:
        column_dict[column] = sorted(set(column_dict[column]))[0]

    return column_dict