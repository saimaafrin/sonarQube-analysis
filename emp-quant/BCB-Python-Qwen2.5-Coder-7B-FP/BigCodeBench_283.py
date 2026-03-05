import os
import json
from collections import Counter
def task_func(json_files_path='./json_files/', key='name'):
    """
    Counts the occurrence of a particular key in all JSON files in a specified directory.

    Args:
    json_files_path (str): The path to the directory containing JSON files.
    key (str): The key to count occurrences of.

    Returns:
    dict: A dictionary with values of the key as keys and their counts as values.
    """
    count_dict = Counter()
    
    # Walk through all files in the directory
    for root, dirs, files in os.walk(json_files_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    # Count occurrences of the key
                    if key in data:
                        count_dict[data[key]] += 1
    
    return dict(count_dict)