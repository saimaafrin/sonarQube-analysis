
import json
from glob import glob

def task_func(directory, string):
    json_files = glob(f'{directory}/**/*.json', recursive=True)
    matching_files = []
    for file in json_files:
        with open(file, 'r') as f:
            data = json.load(f)
            if string in data:
                matching_files.append(file)
    return matching_files