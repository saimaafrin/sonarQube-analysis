
import os
import json
from collections import Counter

def task_func(json_files_path='./json_files/', key='name'):
    # Create a dictionary to store the counts
    counts = {}

    # Loop through all the files in the directory
    for file in os.listdir(json_files_path):
        # Open the file and read it as a JSON object
        with open(json_files_path + file, 'r') as f:
            data = json.load(f)

        # Check if the key exists in the file
        if key in data:
            # If it does, increment the count for that key
            counts[data[key]] += 1

    # Return the dictionary of counts
    return counts