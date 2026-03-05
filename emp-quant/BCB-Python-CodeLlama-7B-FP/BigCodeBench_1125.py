import re
import json
import requests
def task_func(myString, token):
    """
    Extracts a URL from a string and sends it to a REST API via a POST request.
    The URL is included in the JSON payload, and an authorization token is used in the headers for API access.
    If multiple URLs are in myString, then use the first one.
    """
    url_pattern = r"https?://\S+"
    url = re.search(url_pattern, myString).group()
    headers = {"Authorization": f"Bearer {token}"}
    data = {"url": url}
    response = requests.post(url, headers=headers, json=data)
    return response.json()