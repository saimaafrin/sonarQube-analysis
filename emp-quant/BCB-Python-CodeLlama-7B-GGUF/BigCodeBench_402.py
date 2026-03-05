
import re
import requests
import json
import csv
import os

# Constants
API_URL = 'https://api.example.com/data'

def task_func(pattern):
    # Make GET request to API
    response = requests.get(API_URL)

    # Extract data from JSON response
    data = response.json()['data']

    # Create a list of matched data
    matched_data = []
    for item in data:
        if re.search(pattern, item):
            matched_data.append(item)

    # Write matched data to CSV file
    with open('matched_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in matched_data:
            writer.writerow(row)

    # Return absolute path to CSV file
    return os.path.abspath('matched_data.csv')