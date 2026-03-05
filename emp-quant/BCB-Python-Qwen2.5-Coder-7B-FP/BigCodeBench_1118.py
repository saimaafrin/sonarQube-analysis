import json
import csv
import requests
from io import StringIO
CSV_URL = 'https://example.com/data.csv'
JSON_FILE = 'data.json'
def task_func(csv_url=CSV_URL, json_file_path=JSON_FILE):
    # Download the CSV file
    response = requests.get(csv_url)
    response.raise_for_status()  # Check if the request was successful

    # Read the CSV file using StringIO
    csv_file = StringIO(response.text)

    # Convert CSV to JSON
    data = []
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

    # Write JSON to file
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    return json_file_path