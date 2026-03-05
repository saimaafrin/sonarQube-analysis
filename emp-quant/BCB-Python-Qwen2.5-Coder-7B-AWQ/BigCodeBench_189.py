import re
import json
import requests
def task_func(data_url: str) -> list:
    try:
        response = requests.get(data_url)
        data = response.text
        # Extract names using regex, ignoring names inside square brackets
        names = re.findall(r'"(?!\[)([^"]+)(?<!\[)"', data)
        return names
    except Exception:
        return "Invalid url input"