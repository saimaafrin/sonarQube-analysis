
import re
import json
import requests

def task_func(data_url: str) -> list:
    try:
        response = requests.get(data_url)
        data = response.json()
        names = re.findall(r'[A-Z][a-z]*', data)
        return names
    except requests.exceptions.RequestException:
        return "Invalid url input"