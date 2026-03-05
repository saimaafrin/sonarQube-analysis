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
        for key, value in data.items():
            if isinstance(value, str):
                names.append(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, str):
                        names.append(item)
            elif isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    if isinstance(sub_value, str):
                        names.append(sub_value)
                    elif isinstance(sub_value, list):
                        for sub_item in sub_value:
                            if isinstance(sub_item, str):
                                names.append(sub_item)
        return names
    except Exception:
        return "Invalid url input"
data_url = "https://jsonplaceholder.typicode.com/users"