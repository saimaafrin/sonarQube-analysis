import re
import json
import requests
def task_func(data_url: str) -> list:
    """
    Fetch data from a specific URL and extract all names from the JSON-formatted data that are not enclosed by square brackets.
    No specific status code should be raised.
    """
    try:
        response = requests.get(data_url)
        data = response.json()
        names = []
        for name in data:
            if not re.search(r'\[.*\]', name):
                names.append(name)
        return names
    except Exception as e:
        print(f"Invalid url input: {data_url}")
        return []