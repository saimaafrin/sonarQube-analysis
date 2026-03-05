import requests
from PIL import Image
import io
def task_func(url):
    try:
        # Send a GET request to the URL with a timeout of 5 seconds
        response = requests.get(url, timeout=5)
        
        # Check if the response status code is in the 200-299 range
        if not 200 <= response.status_code < 300:
            raise ValueError("The response from the server is not a successful HTTP status code.")
        
        # Check if the content type of the response is an image
        if not response.headers.get('Content-Type').startswith('image'):
            raise ValueError("The content fetched from the URL is not a valid image format.")
        
        # Convert the response content to a PIL Image object
        image = Image.open(io.BytesIO(response.content))
        
        return image
    except requests.exceptions.RequestException as e:
        # Handle exceptions that may occur during the HTTP request
        raise ValueError("The URL is invalid or cannot be reached within the timeout period.") from e