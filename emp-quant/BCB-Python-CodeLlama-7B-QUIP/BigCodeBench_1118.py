
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
    # Convert the CSV file to a StringIO object
    csv_string = StringIO(response.content)
    # Convert the StringIO object to a JSON object
    json_string = csv.DictReader(csv_string)
    # Save the JSON object to a file
    with open(json_file_path, 'w') as json_file:
        json.dump(json_string, json_file)
    return json_file_path