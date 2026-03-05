import os
import json
from collections import Counter
def task_func(json_files_path='./json_files/', key='name'):
    """
    Count the occurrence of a particular key in all json files in a specified directory and return a dictionary with the values of the specified key and their counts.
    """
    # Create a dictionary to store the counts
    counts = {}

    # Iterate over all files in the directory
    for filename in os.listdir(json_files_path):
        # Open the file and read its contents
        with open(os.path.join(json_files_path, filename), 'r') as f:
            data = json.load(f)

        # Extract the value of the specified key from the data
        value = data[key]

        # Increment the count for the value
        counts[value] = counts.get(value, 0) + 1

    # Return the dictionary with the counts
    return counts