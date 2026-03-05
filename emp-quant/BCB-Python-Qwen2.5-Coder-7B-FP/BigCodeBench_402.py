import re
import requests
import json
import csv
import os
API_URL = 'https://api.example.com/data'
def task_func(pattern):
    # Make a GET request to the API
    response = requests.get(API_URL)
    data = response.json()
    
    # Extract data that matches the RegEx pattern
    matched_data = [item for item in data['data'] if re.search(pattern, item)]
    
    # Write the matched data to a CSV file
    csv_file_path = os.path.abspath('matched_data.csv')
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Matched Data'])
        for item in matched_data:
            writer.writerow([item])
    
    # Return the absolute path to the CSV file
    return csv_file_path