
import json
import csv

def task_func(json_file, csv_file):
    # Read the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Open the CSV file for writing
    with open(csv_file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        
        # Write the headers to the CSV file
        headers = data[0].keys()
        csv_writer.writerow(headers)
        
        # Write the data to the CSV file
        for item in data:
            csv_writer.writerow(item.values())
    
    # Return the path to the CSV file
    return csv_file