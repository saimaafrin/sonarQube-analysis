import json
import csv
import requests
from io import StringIO
CSV_URL = 'https://example.com/data.csv'
JSON_FILE = 'data.json'
def task_func(csv_url=CSV_URL, json_file_path=JSON_FILE):
    # Download the CSV file
    response = requests.get(csv_url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Read the CSV file into a StringIO object
    csv_file = StringIO(response.text)

    # Read the CSV data into a list of dictionaries
    csv_data = list(csv.DictReader(csv_file))

    # Convert the list of dictionaries to JSON format
    json_data = json.dumps(csv_data, indent=4)

    # Write the JSON data to a file
    with open(json_file_path, 'w') as json_file:
        json_file.write(json_data)

    # Return the path to the saved JSON file
    return json_file_path