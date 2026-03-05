import csv
import json
import os
def task_func(file_name):
    # Check if the file exists
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"The file {file_name} does not exist.")
    
    # Create a new json file name
    json_file_name = os.path.splitext(file_name)[0] + '.json'
    
    # Read the csv file and convert it to a list of dictionaries
    with open(file_name, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)
    
    # Write the data to a json file
    with open(json_file_name, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    
    # Return the name of the created json file
    return json_file_name