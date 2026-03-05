import requests
from PIL import Image
import io
def task_func(url):
    try:
        # Send a GET request to the URL with a timeout of 5 seconds
        response = requests.get(url, timeout=5)
        
        # Check if the response status code is successful (200-299)
        if not 200 <= response.status_code < 300:
            raise ValueError("The server returned an unsuccessful status code.")
        
        # Check if the content type is an image
        if 'image' not in response.headers.get('Content-Type', ''):
            raise ValueError("The content fetched is not a valid image format.")
        
        # Convert the response content to a PIL Image object
        image = Image.open(io.BytesIO(response.content))
        
        return image
    except requests.exceptions.RequestException as e:
        # Handle exceptions related to the request (e.g., invalid URL, timeout)
        raise ValueError("The URL is invalid or cannot be reached within the timeout period.") from e
    except IOError:
        # Handle exceptions related to image processing
        raise ValueError("The content fetched is not a valid image format that can be handled by PIL.") from e