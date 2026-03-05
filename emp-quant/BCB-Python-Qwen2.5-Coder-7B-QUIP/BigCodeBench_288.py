
import collections
import json
import os

def task_func(directory_path: str) -> dict:
    key_counts = collections.defaultdict(int)
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            with open(os.path.join(directory_path, filename), 'r') as file:
                data = json.load(file)
                for key in data:
                    key_counts[key] += 1
    return dict(key_counts)