
import json
from glob import glob

def task_func(directory, string):
    file_paths = []
    for file_path in glob(directory + '/**/*.json', recursive=True):
        with open(file_path, 'r') as f:
            data = json.load(f)
            if string in data:
                file_paths.append(file_path)
    return file_paths