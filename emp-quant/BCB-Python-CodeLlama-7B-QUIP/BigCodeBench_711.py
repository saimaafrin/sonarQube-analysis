
import json
import csv

def task_func(json_file, csv_file):
    with open(json_file, "r") as f:
        data = json.load(f)
    with open(csv_file, "w") as f:
        writer = csv.DictWriter(f, data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    return csv_file