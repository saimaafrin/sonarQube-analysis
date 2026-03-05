import os
import json
from collections import Counter
def task_func(json_files_path='./json_files/', key='name'):
    """
    Counts the occurrence of a particular key in all json files in a specified directory.

    Args:
    json_files_path (str): The path to the directory containing the JSON files.
    key (str): The key to count occurrences of.

    Returns:
    dict: A dictionary with values of the key as keys and their counts as values.
    """
    count_dict = Counter()
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(json_files_path):
        if filename.endswith('.json'):
            file_path = os.path.join(json_files_path, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Count occurrences of the specified key
                count_dict.update(data.get(key, []))
    
    return dict(count_dict)