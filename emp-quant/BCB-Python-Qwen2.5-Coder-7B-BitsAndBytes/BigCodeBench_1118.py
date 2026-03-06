
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
    if response.status_code != 200:
        raise Exception(f"Failed to download CSV file: {response.status_code}")
    
    # Read the CSV content
    csv_content = response.text
    
    # Convert CSV to JSON
    reader = csv.DictReader(StringIO(csv_content))
    data = list(reader)
    
    # Write JSON to file
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    return json_file_path