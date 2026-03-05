
import os
import json
from collections import Counter

def task_func(json_files_path='./json_files/', key='name'):
    """
    Count the occurrence of a particular key in all json files in a specified directory and return a dictionary with the values of the specified key and their counts.

    Args:
        json_files_path (str): Path to the directory containing the json files.
        key (str): Key to count the occurrences of.

    Returns:
        dict: A dictionary with values of the key as keys and their counts as values.
    """
    file_paths = [os.path.join(json_files_path, file) for file in os.listdir(json_files_path)]
    data = [json.load(open(file_path)) for file_path in file_paths]
    counts = Counter([item[key] for item in data])
    return counts