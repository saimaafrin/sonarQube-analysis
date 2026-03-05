import csv
import json
import os
def task_func(file_name):
    # Check if the file exists
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"The file {file_name} does not exist.")
    
    # Create a dictionary to store the data
    data = []
    
    # Open the CSV file and read the data
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    
    # Create a JSON file and write the data
    json_file_name = os.path.splitext(file_name)[0] + '.json'
    with open(json_file_name, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    
    # Return the name of the created JSON file
    return json_file_name