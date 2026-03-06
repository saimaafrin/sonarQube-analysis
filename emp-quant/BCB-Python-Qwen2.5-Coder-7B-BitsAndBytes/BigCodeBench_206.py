
import csv
import json
import os

def task_func(file_name):
    # Check if the CSV file exists
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"The file {file_name} does not exist.")
    
    # Read data from CSV
    with open(file_name, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    
    # Create JSON file name
    json_file_name = os.path.splitext(file_name)[0] + '.json'
    
    # Write data to JSON
    with open(json_file_name, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)
    
    return json_file_name