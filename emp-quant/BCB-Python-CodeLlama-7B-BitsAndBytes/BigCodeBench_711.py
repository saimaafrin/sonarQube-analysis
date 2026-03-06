
import json
import csv

def task_func(json_file, csv_file):
    # Open the JSON file and read its contents
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Open the CSV file and write the header row
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data[0].keys())

    # Write the data rows
    for row in data:
        writer.writerow(row.values())

    return csv_file