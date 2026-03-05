
import re
import json
import requests

def task_func(data_url: str) -> list:
    try:
        response = requests.get(data_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        # Assuming the names are under a key called 'names' and are in a list
        names = data['names']
        # Using regular expression to find names not enclosed in square brackets
        pattern = re.compile(r'\b\w+\b')
        extracted_names = [name for name in names if not re.search(r'\[|\]', name)]
        return extracted_names
    except (requests.RequestException, KeyError) as e:
        return "Invalid url input"