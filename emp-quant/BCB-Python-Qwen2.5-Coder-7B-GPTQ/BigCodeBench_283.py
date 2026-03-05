import os
import json
from collections import Counter
def task_func(json_files_path='./json_files/', key='name'):
    # Initialize a Counter object to store the counts of each value
    value_counts = Counter()
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(json_files_path):
        if filename.endswith('.json'):  # Check if the file is a JSON file
            file_path = os.path.join(json_files_path, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Check if the key exists in the JSON data
                if key in data:
                    value_counts[data[key]] += 1
    
    # Convert the Counter object to a dictionary and return
    return dict(value_counts)