
import collections
import json
import os

def task_func(directory_path: str) -> dict:
    # Initialize a Counter to keep track of key appearances
    key_counter = collections.Counter()
    
    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    # Flatten the JSON data and count each key
                    flatten_json(data, key_counter)
    
    # Convert the Counter to a dictionary
    result_dict = dict(key_counter)
    return result_dict

def flatten_json(y, counter):
    for i in y.keys():
        if isinstance(y[i], dict):
            flatten_json(y[i], counter)
        else:
            counter[i] += 1