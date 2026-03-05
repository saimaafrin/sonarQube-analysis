import json
import csv
import requests
from io import StringIO
CSV_URL = 'https://example.com/data.csv'
JSON_FILE = 'data.json'
def task_func(csv_url=CSV_URL, json_file_path=JSON_FILE):
    # Download the CSV file
    response = requests.get(csv_url)
    # Convert the CSV file to a JSON file
    csv_data = StringIO(response.text)
    json_data = csv.reader(csv_data)
    json_data = json.dumps(json_data)
    # Save the JSON file
    with open(json_file_path, 'w') as f:
        f.write(json_data)
    return json_file_path