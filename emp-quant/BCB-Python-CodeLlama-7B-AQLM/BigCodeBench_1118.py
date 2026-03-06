import json
import csv
import requests
from io import StringIO
CSV_URL = 'https://example.com/data.csv'
JSON_FILE = 'data.json'
def task_func(csv_url=CSV_URL, json_file_path=JSON_FILE):
    """
    Downloads a CSV file from a specified URL, converts it to JSON format, and saves it to a specified file path.
    
    Parameters:
    - csv_url (str): The URL from which the CSV data should be downloaded. Defaults to a constant CSV_URL.
    - json_file_path (str): The file path where the JSON data should be saved. Defaults to a constant JSON_FILE.

    Returns:
    str: The path to the saved JSON file.

    Requirements:
    - json
    - csv
    - requests
    - io.StringIO

    Example:
    >>> task_func("https://example.com/sample.csv", "sample.json")
    "sample.json"
    """
    # Download the CSV file
    response = requests.get(csv_url)
    csv_data = response.text

    # Convert the CSV data to JSON
    json_data = csv_to_json(csv_data)

    # Save the JSON data to a file
    save_json(json_data, json_file_path)

    # Return the path to the saved JSON file
    return json_file_path