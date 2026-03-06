
import json
import csv
import os
import base64

def task_func(raw_string, filename, output_dir):
    # Decode the base64-encoded JSON string
    decoded_json = base64.b64decode(raw_string).decode('utf-8')

    # Load the JSON data into a Python dictionary
    data = json.loads(decoded_json)

    # Create a CSV file in the output directory with the given filename
    file_path = os.path.join(output_dir, filename)
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(data.keys())

        # Write the data rows
        for row in data.values():
            writer.writerow(row)

    return file_path