import csv
import json
import os
def task_func(file_name):
    """
    Convert a csv file to a json file.
    """
    try:
        with open(file_name, 'r') as csv_file:
            reader = csv.reader(csv_file)
            data = list(reader)
            with open(file_name + '.json', 'w') as json_file:
                json.dump(data, json_file)
                return file_name + '.json'
    except FileNotFoundError:
        raise FileNotFoundError(f'File {file_name} does not exist')