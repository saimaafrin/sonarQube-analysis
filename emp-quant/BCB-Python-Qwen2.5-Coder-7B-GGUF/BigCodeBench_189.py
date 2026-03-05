
import re
import json
import requests

def task_func(data_url: str) -> list:
    try:
        response = requests.get(data_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        names = re.findall(r'"(?!.*\[\].*?)(?:"[^"]*"[^"]*")', json.dumps(data))
        return [name.strip('"') for name in names]
    except requests.RequestException:
        return "Invalid url input"