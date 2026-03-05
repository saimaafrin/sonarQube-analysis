import json
import csv
import os
import base64
def task_func(raw_string, filename, output_dir):
    """
    Processes a base64-encoded JSON string, stores the data in a CSV file, and returns the path of the file.
    """
    # Decode the base64-encoded JSON string
    decoded_string = base64.b64decode(raw_string).decode("utf-8")
    # Load the JSON data into a Python dictionary
    data = json.loads(decoded_string)
    # Create a CSV file with the data
    with open(os.path.join(output_dir, filename), "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        writer.writeheader()
        for row in data.values():
            writer.writerow(row)
    # Return the path of the CSV file
    return os.path.join(output_dir, filename)
raw_string = "eyJrZXkiOiAidmFsdWUiOiAidmFsdWUifQ=="
filename = "data.csv"
output_dir = "output"