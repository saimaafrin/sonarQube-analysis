
import csv
import json
import os

def task_func(file_name):
    try:
        # Check if the file exists
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"The file {file_name} does not exist.")
        
        # Read the CSV file
        with open(file_name, mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
        
        # Create the JSON file name
        json_file_name = os.path.splitext(file_name)[0] + '.json'
        
        # Write the data to the JSON file
        with open(json_file_name, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        return json_file_name
    except FileNotFoundError as e:
        raise e