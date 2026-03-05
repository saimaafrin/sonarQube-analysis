import re
import json
import requests
def task_func(data_url: str) -> list:
    try:
        response = requests.get(data_url)
        data = response.text
        # Extract names that are not enclosed by square brackets
        names = re.findall(r'(?<!\[)\b\w+\b(?!\])', data)
        return names
    except Exception:
        return "Invalid url input"