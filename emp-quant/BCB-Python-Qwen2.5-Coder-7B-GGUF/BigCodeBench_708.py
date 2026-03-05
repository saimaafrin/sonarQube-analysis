
import json
import csv
import os
import base64

def task_func(raw_string, filename, output_dir):
    # Decode the base64-encoded string
    decoded_bytes = base64.b64decode(raw_string)
    decoded_string = decoded_bytes.decode('utf-8')
    
    # Load the JSON data
    data = json.loads(decoded_string)
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Define the file path
    file_path = os.path.join(output_dir, filename)
    
    # Write the data to a CSV file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the headers
        writer.writerow(data[0].keys())
        # Write the data rows
        for item in data:
            writer.writerow(item.values())
    
    # Return the file path
    return file_path