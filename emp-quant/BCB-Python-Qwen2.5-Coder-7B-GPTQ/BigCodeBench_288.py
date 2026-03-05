import collections
import json
import os
def task_func(directory_path: str) -> dict:
    # Initialize a counter to keep track of key appearances
    key_counter = collections.Counter()
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Check if the file is a JSON file
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                # Open and load the JSON file
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    # Update the counter with keys from the JSON data
                    key_counter.update(data)
    
    # Convert the counter to a dictionary and return
    return dict(key_counter)