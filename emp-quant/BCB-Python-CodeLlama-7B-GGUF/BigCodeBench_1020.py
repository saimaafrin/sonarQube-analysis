
import json
import requests
import chardet

# Constants
API_URL = "http://api.example.com/data"

def task_func(url=API_URL, from_encoding=None, to_encoding="utf8"):
    # Initiate an HTTP GET request to the specified URL with a 5-second timeout
    response = requests.get(url, timeout=5)

    # Check if the response content is empty
    if not response.content:
        return {}

    # Detect the encoding of the response content
    encoding = chardet.detect(response.content)["encoding"]

    # Decode the response content using the detected encoding
    decoded_content = response.content.decode(encoding)

    # Re-encode the decoded content using the specified encoding
    reencoded_content = decoded_content.encode(to_encoding)

    # Parse the re-encoded content as JSON
    try:
        json_data = json.loads(reencoded_content)
    except ValueError as e:
        raise ValueError("Unable to detect encoding for non-empty content") from e

    return json_data