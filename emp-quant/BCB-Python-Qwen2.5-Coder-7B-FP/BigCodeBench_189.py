import re
import json
import requests
def task_func(data_url: str) -> list:
    try:
        response = requests.get(data_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        names = re.findall(r'"(?!.*\[\])([^"]+)"', json.dumps(data))
        return names
    except requests.RequestException:
        return "Invalid url input"