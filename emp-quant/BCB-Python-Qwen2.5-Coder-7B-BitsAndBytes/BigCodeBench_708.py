
import json
import csv
import os
import base64

def task_func(raw_string, filename, output_dir):
    # Decode the base64 encoded string to get the JSON data
    decoded_data = base64.b64decode(raw_string).decode('utf-8')
    
    # Load the JSON data into a Python dictionary
    data = json.loads(decoded_data)
    
    # Create the full output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Construct the full file path
    file_path = os.path.join(output_dir, filename + '.csv')
    
    # Write the data to a CSV file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Assuming the data is a list of dictionaries
        headers = data[0].keys()
        writer.writerow(headers)
        
        for item in data:
            writer.writerow(item.values())
    
    return file_path