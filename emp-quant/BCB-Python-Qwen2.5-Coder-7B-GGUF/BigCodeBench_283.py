
import os
import json
from collections import Counter

def task_func(json_files_path='./json_files/', key='name'):
    count_dict = Counter()
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(json_files_path):
        if filename.endswith('.json'):
            file_path = os.path.join(json_files_path, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Count occurrences of the specified key
                if key in data:
                    count_dict[data[key]] += 1
    
    return dict(count_dict)