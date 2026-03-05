
import json
import pandas as pd

def task_func(result, csv_file_path="test.csv", json_file_path="test.json"):
    # Save the list of dictionaries to a CSV file
    with open(csv_file_path, "w") as csv_file:
        csv_writer = csv.DictWriter(csv_file, result)
        csv_writer.writeheader()
        csv_writer.writerows(result)

    # Save the list of dictionaries to a JSON file
    with open(json_file_path, "w") as json_file:
        json.dump(result, json_file)

    return None