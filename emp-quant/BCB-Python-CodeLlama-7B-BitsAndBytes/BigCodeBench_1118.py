
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
    csv_data = response.content

    # Convert the CSV data to a JSON object
    json_data = csv.DictReader(StringIO(csv_data.decode('utf-8')))
    json_data = json.dumps(json_data)

    # Save the JSON data to a file
    with open(json_file_path, 'w') as f:
        f.write(json_data)

    # Return the path to the saved JSON file
    return json_file_path

# Call the function and print the output
print(task_func())