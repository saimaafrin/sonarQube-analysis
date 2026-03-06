import re
import requests
import json
import csv
import os
API_URL = 'https://api.example.com/data'
def task_func(pattern):
    """
    Make a GET request to an API, extract data that matches a RegEx pattern, and write it to a CSV file.

    Parameters:
    pattern (str): The regex pattern to match.

    Returns:
    str: The absolute path to the CSV file containing matched data. If no data is matched, the file will be empty.

    Note:
    - The CSV file generated name is "matched_data.csv"
    - The JSON response from the GET request in the API contains a key named "data", from which the data is extracted.

    Requirements:
    - requests
    - json
    - csv
    - re
    - os

    Example:
    >>> task_func(r'\\\\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\\\\.[A-Z]{2,}\\\\b')
    '/absolute/path/to/matched_data.csv'
    >>> task_func(r'\\\\d{3}-\\\\d{2}-\\\\d{4}')  # For matching SSN format
    '/absolute/path/to/matched_data.csv'
    """
    # Make a GET request to the API
    response = requests.get(API_URL)
    # Extract the data from the response
    data = response.json()['data']
    # Create a list of matched data
    matched_data = []
    # Iterate over the data
    for item in data:
        # Check if the item matches the pattern
        if re.search(pattern, item):
            # If it matches, append it to the list
            matched_data.append(item)
    # Write the matched data to a CSV file
    with open('matched_data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(matched_data)
    # Return the absolute path to the CSV file
    return os.path.abspath('matched_data.csv')