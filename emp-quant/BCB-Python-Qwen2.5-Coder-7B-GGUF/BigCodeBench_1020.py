
import json
import requests
import chardet

# Constants
API_URL = "http://api.example.com/data"

def task_func(url=API_URL, from_encoding=None, to_encoding="utf8"):
    try:
        # Send HTTP GET request with a timeout of 5 seconds
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Get the raw bytes of the response content
        content = response.content

        # Handle empty content
        if not content:
            return {}

        # Detect encoding if not provided
        if not from_encoding:
            result = chardet.detect(content)
            from_encoding = result['encoding']

        # Decode the content using the detected encoding
        decoded_content = content.decode(from_encoding)

        # Re-encode the content using the specified to_encoding
        re_encoded_content = decoded_content.encode(to_encoding)

        # Parse the JSON data
        json_data = json.loads(re_encoded_content.decode(to_encoding))

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"HTTP Request Error: {e}")
        return {}
    except ValueError as e:
        print(f"ValueError: {e}")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}