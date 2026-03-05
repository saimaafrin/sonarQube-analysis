
import os
import json
from collections import Counter

def task_func(json_files_path='./json_files/', key='name'):
    count_dict = Counter()
    
    # Walk through the directory
    for root, dirs, files in os.walk(json_files_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    if key in data:
                        count_dict[data[key]] += 1
    
    return dict(count_dict)