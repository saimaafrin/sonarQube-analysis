import json
import requests
import chardet
API_URL = "http://api.example.com/data"
def task_func(url=API_URL, from_encoding=None, to_encoding="utf8"):
    """
    Fetches data from a specified REST API URL and processes it for JSON parsing.
    Handles different encoding scenarios and raises exceptions for specific errors.
    """
    try:
        # Send HTTP GET request with a timeout of 5 seconds
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        # Get the content of the response in raw bytes
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

        # Re-encode the content to the target encoding
        reencoded_content = decoded_content.encode(to_encoding)

        # Decode the re-encoded content back to a string
        final_content = reencoded_content.decode(to_encoding)

        # Parse the JSON content
        json_data = json.loads(final_content)

        return json_data

    except requests.exceptions.RequestException as e:
        # Handle request-related errors
        print(f"Request error: {e}")
        return {}

    except ValueError as e:
        # Handle JSON parsing errors
        print(f"JSON parsing error: {e}")
        return {}

    except Exception as e:
        # Handle other exceptions
        print(f"An unexpected error occurred: {e}")
        return {}