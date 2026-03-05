import json
import csv
def task_func(json_file, csv_file):
    # Read the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Write the data to a CSV file
    with open(csv_file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        # Write the header (keys of the first item)
        csv_writer.writerow(data[0].keys())
        # Write the data rows
        for item in data:
            csv_writer.writerow(item.values())
    
    # Return the path to the CSV file
    return csv_file