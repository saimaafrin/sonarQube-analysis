
import json
from glob import glob

def task_func(directory, string):
    matching_files = []
    for json_file in glob.glob(f"{directory}/**/*", recursive=True):
        if json_file.endswith('.json'):
            with open(json_file, 'r') as file:
                data = json.load(file)
                if search_in_json(data, string):
                    matching_files.append(json_file)
    return matching_files

def search_in_json(data, string):
    if isinstance(data, dict):
        for key, value in data.items():
            if search_in_json(value, string):
                return True
    elif isinstance(data, list):
        for item in data:
            if search_in_json(item, string):
                return True
    elif isinstance(data, str) and string in data:
        return True
    return False