
import json
import csv
import os
import base64

def task_func(raw_string, filename, output_dir):
    # Decode the base64-encoded JSON string
    decoded_string = base64.b64decode(raw_string).decode('utf-8')

    # Load the JSON data into a Python dictionary
    data = json.loads(decoded_string)

    # Create a CSV file in the output directory
    file_path = os.path.join(output_dir, filename)
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the data to the CSV file
        for key, value in data.items():
            writer.writerow([key, value])

    return file_path