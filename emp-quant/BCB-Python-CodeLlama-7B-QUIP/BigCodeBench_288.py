
import collections
import json
import os

def task_func(directory_path: str) -> dict:
    # Create a dictionary to store the counts of each key
    counts = collections.defaultdict(int)

    # Loop through all files in the directory
    for file_name in os.listdir(directory_path):
        # Open the file and read its contents
        with open(os.path.join(directory_path, file_name), 'r') as f:
            data = json.load(f)

        # Loop through each key in the data
        for key in data:
            # Increment the count for this key
            counts[key] += 1

    # Return the counts dictionary
    return counts