
import os
import json
from collections import Counter

def task_func(json_files_path='./json_files/', key='name'):
    # Create a dictionary to store the counts of the specified key
    counts = {}

    # Iterate over all JSON files in the specified directory
    for filename in os.listdir(json_files_path):
        # Open the JSON file and load it into a dictionary
        with open(os.path.join(json_files_path, filename), 'r') as f:
            data = json.load(f)

        # Extract the value of the specified key from the dictionary
        value = data[key]

        # Increment the count of the value in the dictionary
        counts[value] = counts.get(value, 0) + 1

    # Return the dictionary with the counts of the specified key
    return counts