import json
import requests
import chardet
API_URL = "http://api.example.com/data"
def task_func(url=API_URL, from_encoding=None, to_encoding="utf8"):
    """
    Fetches data from a specified REST API URL and processes it for JSON parsing.
    The process involves decoding and re-encoding the data, handling different encoding scenarios.
    """
    # Initiate an HTTP GET request to the specified URL with a 5-second timeout
    response = requests.get(url, timeout=5)

    # Retrieve the response content in raw bytes
    content = response.content

    # Handle cases with empty content and undetectable encoding
    if not content:
        return {}
    elif not from_encoding:
        from_encoding = chardet.detect(content)["encoding"]
        if not from_encoding:
            raise ValueError("Unable to detect encoding for non-empty content")

    # Decode the content using the detected encoding
    decoded_content = content.decode(from_encoding)

    # Re-encode the decoded content using the specified encoding
    reencoded_content = decoded_content.encode(to_encoding)

    # Parse the reencoded content as JSON
    try:
        json_data = json.loads(reencoded_content)
    except json.JSONDecodeError:
        raise ValueError("Failed to parse JSON data")

    return json_data