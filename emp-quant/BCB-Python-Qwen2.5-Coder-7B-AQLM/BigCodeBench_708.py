
import json
import csv
import os
import base64

def task_func(raw_string, filename, output_dir):
    # Decode the base64-encoded string
    decoded_string = base64.b64decode(raw_string).decode('utf-8')
    
    # Parse the JSON string
    data = json.loads(decoded_string)
    
    # Create the full path for the output CSV file
    file_path = os.path.join(output_dir, filename)
    
    # Write the data to a CSV file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Assuming the data is a list of dictionaries
        for item in data:
            writer.writerow(item.values())
    
    # Return the path of the file
    return file_path