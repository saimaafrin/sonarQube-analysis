
import os
import json
from collections import Counter

def task_func(json_files_path='./json_files/', key='name'):
    # Initialize a Counter to hold the counts of each value
    value_counts = Counter()

    # Iterate over all files in the specified directory
    for filename in os.listdir(json_files_path):
        if filename.endswith('.json'):
            # Open and load the JSON file
            with open(os.path.join(json_files_path, filename), 'r') as file:
                data = json.load(file)
                # Extract the values associated with the specified key
                values = data.get(key, [])
                # Update the Counter with the values
                value_counts.update(values)

    # Return the resulting dictionary
    return dict(value_counts)