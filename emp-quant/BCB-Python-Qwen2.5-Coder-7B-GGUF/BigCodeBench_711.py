
import json
import csv

def task_func(json_file, csv_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    with open(csv_file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        headers = data[0].keys()
        csv_writer.writerow(headers)
        for item in data:
            csv_writer.writerow(item.values())
    
    return csv_file