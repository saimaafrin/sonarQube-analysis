
import json
import requests
import chardet

# Constants
API_URL = "http://api.example.com/data"

def task_func(url=API_URL, from_encoding=None, to_encoding="utf8"):
    # Set a timeout of 5 seconds for the API request
    response = requests.get(url, timeout=5)
    
    # Check if the response content is empty
    if not response.content:
        return {}
    
    # Detect the encoding of the response content
    result = chardet.detect(response.content)
    encoding = result['encoding']
    
    # If encoding is not detectable, raise an exception
    if encoding is None:
        raise ValueError("Unable to detect encoding for non-empty content")
    
    # Decode the response content using the detected encoding
    decoded_content = response.content.decode(encoding)
    
    # Re-encode the decoded content using the specified encoding
    encoded_content = decoded_content.encode(to_encoding)
    
    # Decode the re-encoded content back to a string
    final_content = encoded_content.decode(to_encoding)
    
    # Parse the final content as JSON
    json_data = json.loads(final_content)
    
    return json_data