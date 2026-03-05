
import json
import requests
import chardet
# Constants
API_URL = "http://api.example.com/data"

def task_func(url=API_URL, from_encoding=None, to_encoding="utf8"):
    # Initiate the HTTP GET request with a 5-second timeout
    response = requests.get(url, timeout=5)
    # Check for empty content
    if not response.content:
        return {}
    # Check for undetectable encoding
    try:
        encoding = chardet.detect(response.content)
    except ValueError:
        raise ValueError("Unable to detect encoding for non-empty content")
    # Decode the response content
    content = response.content.decode(encoding)
    # Re-encode the content in UTF-8
    content = content.encode("utf8")
    # Parse the JSON data
    data = json.loads(content)
    return data