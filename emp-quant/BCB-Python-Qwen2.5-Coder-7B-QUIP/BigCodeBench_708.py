
import json
import csv
import os
import base64

def task_func(raw_string, filename, output_dir):
    # Decode the base64-encoded JSON string
    json_data = json.loads(base64.b64decode(raw_string).decode('utf-8'))
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Define the output file path
    file_path = os.path.join(output_dir, filename)
    
    # Write the JSON data to a CSV file
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in json_data.items():
            writer.writerow([key, value])
    
    # Return the path of the file
    return file_path