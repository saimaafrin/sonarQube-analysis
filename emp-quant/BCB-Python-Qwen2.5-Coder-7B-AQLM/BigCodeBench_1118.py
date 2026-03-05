
import json
import csv
import requests
from io import StringIO

# Constants
CSV_URL = 'https://example.com/data.csv'
JSON_FILE = 'data.json'

def task_func(csv_url=CSV_URL, json_file_path=JSON_FILE):
    # Download the CSV file
    response = requests.get(csv_url)
    response.raise_for_status()  # Check if the request was successful

    # Read the CSV content
    csv_content = response.text

    # Convert CSV to JSON
    csv_file = StringIO(csv_content)
    csv_reader = csv.DictReader(csv_file)
    json_data = list(csv_reader)

    # Write JSON data to a file
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    return json_file_path