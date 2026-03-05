
import json
import csv

def task_func(json_file, csv_file):
    # Read the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Write the CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.keys())
        writer.writerow(data.values())
    
    return csv_file