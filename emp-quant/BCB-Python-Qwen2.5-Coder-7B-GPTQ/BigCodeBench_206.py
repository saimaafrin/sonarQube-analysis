import csv
import json
import os
def task_func(file_name):
    # Check if the file exists
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"The file {file_name} does not exist.")
    
    # Create a new JSON file name
    json_file_name = os.path.splitext(file_name)[0] + '.json'
    
    # Read the CSV file and convert it to a list of dictionaries
    data = []
    with open(file_name, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    
    # Write the data to a JSON file
    with open(json_file_name, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    
    # Return the name of the created JSON file
    return json_file_name