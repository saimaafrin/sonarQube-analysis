import json
import csv
import requests
from io import StringIO
CSV_URL = 'https://example.com/data.csv'
JSON_FILE = 'data.json'
def task_func(csv_url=CSV_URL, json_file_path=JSON_FILE):
    # Download CSV file
    response = requests.get(csv_url)
    csv_data = response.content.decode('utf-8')
    # Convert CSV to JSON
    json_data = csv.DictReader(StringIO(csv_data))
    json_data = [row for row in json_data]
    # Save JSON file
    with open(json_file_path, 'w') as f:
        json.dump(json_data, f)
    return json_file_path