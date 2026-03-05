import requests
from PIL import Image
import io
def task_func(url):
    try:
        # Set a timeout of 5 seconds for the HTTP request
        response = requests.get(url, timeout=5)
        
        # Check if the response status code is successful
        if not (200 <= response.status_code < 300):
            raise ValueError("The server returned a non-successful status code.")
        
        # Check if the content is a valid image format
        image = Image.open(io.BytesIO(response.content))
        
        return image
    except requests.exceptions.RequestException as e:
        # Handle exceptions related to the request (e.g., invalid URL, timeout)
        raise ValueError("Failed to fetch the image due to an error: " + str(e))
    except IOError:
        # Handle cases where the content is not a valid image format
        raise ValueError("The fetched content is not a valid image format.")