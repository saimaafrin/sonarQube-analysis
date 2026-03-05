
import collections
import json
import os

def task_func(directory_path: str) -> dict:
    key_counts = collections.defaultdict(int)
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    # Count the occurrences of each key
                    for key in data:
                        key_counts[key] += 1
    
    return dict(key_counts)