import re
import requests
import json
import csv
import os
API_URL = 'https://api.example.com/data'
def task_func(pattern):
    # Make a GET request to the API
    response = requests.get(API_URL)

    # Extract the data from the JSON response
    data = response.json()['data']

    # Create a list to store the matched data
    matched_data = []

    # Iterate over the data and match the pattern
    for item in data:
        if re.search(pattern, item):
            matched_data.append(item)

    # Write the matched data to a CSV file
    with open('matched_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(matched_data)

    # Return the absolute path to the CSV file
    return os.path.abspath('matched_data.csv')