
import os
import json
from collections import Counter

def task_func(json_files_path='./json_files/', key='name'):
    # Initialize a counter to keep track of occurrences
    count_dict = Counter()
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(json_files_path):
        if filename.endswith('.json'):  # Check if the file is a JSON file
            file_path = os.path.join(json_files_path, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Extract the value associated with the specified key
                value = data.get(key, None)
                if value is not None:
                    count_dict[value] += 1
    
    return dict(count_dict)