
import re
import json
import requests

def task_func(data_url: str) -> list:
    """
    Fetch data from a specific URL and extract all names from the JSON-formatted data that are not enclosed by square brackets.

    Args:
        data_url (str): The URL from which to fetch the data.

    Returns:
        list[str]: A list of extracted names.
    """
    try:
        response = requests.get(data_url)
        data = response.json()
    except requests.exceptions.RequestException:
        return "Invalid url input"

    names = []
    pattern = r"(?<!\[)\w+(?!\])"
    for name in re.findall(pattern, json.dumps(data)):
        names.append(name)

    return names