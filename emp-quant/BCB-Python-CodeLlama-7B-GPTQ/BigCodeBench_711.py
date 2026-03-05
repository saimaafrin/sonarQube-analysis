import json
import csv
def task_func(json_file, csv_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
    return csv_file
json_file = 'data.json'
csv_file = 'data.csv'