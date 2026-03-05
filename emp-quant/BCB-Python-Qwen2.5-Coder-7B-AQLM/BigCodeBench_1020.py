
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

        # Get the raw content of the response
        raw_content = response.content

        # Handle empty content
        if not raw_content:
            return {}

        # Detect encoding if not provided
        if not from_encoding:
            encoding_result = chardet.detect(raw_content)
            if encoding_result['confidence'] < 0.9:
                raise ValueError("Unable to detect encoding for non-empty content")
            from_encoding = encoding_result['encoding']

        # Decode the raw content using the detected encoding
        decoded_content = raw_content.decode(from_encoding)

        # Re-encode the content to the target encoding
        reencoded_content = decoded_content.encode(to_encoding)

        # Parse the re-encoded content as JSON
        json_data = json.loads(reencoded_content.decode(to_encoding))

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