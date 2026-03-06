
import json
import requests
import chardet

# Constants
API_URL = "http://api.example.com/data"

def task_func(url=API_URL, from_encoding=None, to_encoding="utf8"):
    try:
        # Send HTTP GET request with a timeout of 5 seconds
        response = requests.get(url, timeout=5)
        
        # Check if the response content is not empty
        if not response.content:
            return {}
        
        # Detect the encoding of the response content
        detected_encoding = chardet.detect(response.content)['encoding']
        
        # If no encoding is detected, raise an exception
        if not detected_encoding:
            raise ValueError("Unable to detect encoding for non-empty content")
        
        # Decode the response content using the detected encoding
        decoded_content = response.content.decode(detected_encoding)
        
        # Re-encode the decoded content to the target encoding (UTF-8)
        encoded_content = decoded_content.encode(to_encoding)
        
        # Decode the re-encoded content back to string
        final_decoded_content = encoded_content.decode(to_encoding)
        
        # Parse the final decoded content as JSON
        json_data = json.loads(final_decoded_content)
        
        return json_data
    
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}