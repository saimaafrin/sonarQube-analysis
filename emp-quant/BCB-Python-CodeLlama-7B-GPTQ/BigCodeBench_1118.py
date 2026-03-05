import json
import csv
import requests
from io import StringIO
CSV_URL = 'https://example.com/data.csv'
JSON_FILE = 'data.json'
def task_func(csv_url=CSV_URL, json_file_path=JSON_FILE):
    # Download the CSV file
    response = requests.get(csv_url)
    csv_data = response.content

    # Convert the CSV data to JSON
    json_data = csv.reader(StringIO(csv_data.decode('utf-8')))
    json_data = [dict(row) for row in json_data]

    # Save the JSON data to a file
    with open(json_file_path, 'w') as f:
        json.dump(json_data, f)

    # Return the path to the saved JSON file
    return json_file_path
csv_url = 'https://example.com/data.csv'
json_file_path = 'data.json'