
import csv
import json
import os

def task_func(file_name):
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"File {file_name} does not exist")

    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)

    with open(file_name.replace('.csv', '.json'), 'w') as json_file:
        json.dump(data, json_file)

    return file_name.replace('.csv', '.json')