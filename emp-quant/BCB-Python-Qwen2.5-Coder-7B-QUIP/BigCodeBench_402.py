
import re
import requests
import json
import csv
import os  

# Constants
API_URL = 'https://api.example.com/data'

def task_func(pattern):
    # Make a GET request to the API
    response = requests.get(API_URL)
    data = response.json()

    # Extract data that matches the RegEx pattern
    matched_data = [item for item in data['data'] if re.match(pattern, item)]

    # Write the matched data to a CSV file
    csv_file_path = 'matched_data.csv'
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Matched Data'])
        for item in matched_data:
            writer.writerow([item])

    # Return the absolute path to the CSV file
    return os.path.abspath(csv_file_path)