
import csv
import json
import os

def task_func(file_name):
    # Check if the file exists
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"The file {file_name} does not exist.")
    
    # Read the CSV file
    with open(file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)
    
    # Convert the data to JSON
    json_file_name = file_name.replace('.csv', '.json')
    with open(json_file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    # Return the name of the created JSON file
    return json_file_name