
import re
import json
import requests

def task_func(data_url: str) -> list:
    try:
        response = requests.get(data_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        
        # Convert the JSON data to a string to use regex
        data_str = json.dumps(data)
        
        # Regular expression to find names not enclosed by square brackets
        pattern = r'(?<!\[)"(.*?)"(?!])'
        matches = re.findall(pattern, data_str)
        
        return matches
    except Exception as e:
        print("Invalid url input")
        return []