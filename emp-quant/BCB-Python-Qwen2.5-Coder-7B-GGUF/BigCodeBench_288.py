
import collections
import json
import os

def task_func(directory_path: str) -> dict:
    key_counts = collections.Counter()
    
    # Walk through all files in the directory
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    # Flatten the JSON data and count keys
                    for key in flatten_json(data):
                        key_counts[key] += 1
    
    return dict(key_counts)

def flatten_json(y):
    out = {}
    
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
    
    flatten(y)
    return out