
import csv
import json
import os

def task_func(file_name):
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            data = [row for row in reader]
            with open(file_name + ".json", "w") as f:
                json.dump(data, f)
                return file_name + ".json"
    except FileNotFoundError:
        raise FileNotFoundError("File not found")