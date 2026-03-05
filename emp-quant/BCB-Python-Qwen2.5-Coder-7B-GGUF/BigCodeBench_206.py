
import csv
import json
import os

def task_func(file_name):
    try:
        # Check if the file exists
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"The file {file_name} does not exist.")
        
        # Read the CSV file
        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)
        
        # Create a JSON file name
        json_file_name = os.path.splitext(file_name)[0] + '.json'
        
        # Write the data to a JSON file
        with open(json_file_name, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        return json_file_name
    except Exception as e:
        raise e