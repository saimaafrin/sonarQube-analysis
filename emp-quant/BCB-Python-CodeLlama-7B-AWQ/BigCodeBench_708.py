import json
import csv
import os
import base64
def task_func(raw_string, filename, output_dir):
    """
    Processes a base64-encoded JSON string, stores the data in a CSV file, and returns the path of the file.
    """
    # Decode the base64-encoded JSON string
    decoded_string = base64.b64decode(raw_string).decode('utf-8')

    # Load the JSON data from the decoded string
    data = json.loads(decoded_string)

    # Create a CSV file with the data
    csv_file = os.path.join(output_dir, filename)
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)

    # Return the path of the CSV file
    return csv_file
raw_string = "eyJ0eXBlIjoiYXNzZXJ0IiwiYm9keSI6Imh0dHA6Ly9teWJhbmdlcm9sZC5jb20iLCJwYXNzd29yZCI6IiJ9"
filename = "data.csv"
output_dir = "output"