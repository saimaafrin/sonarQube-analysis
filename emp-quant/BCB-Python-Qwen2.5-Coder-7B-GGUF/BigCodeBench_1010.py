
import requests
from PIL import Image
import io

def task_func(url):
    try:
        # Set a timeout of 5 seconds for the HTTP request
        response = requests.get(url, timeout=5)
        
        # Check if the response status code is successful
        if not (200 <= response.status_code < 300):
            raise ValueError(f"Failed to retrieve image. HTTP status code: {response.status_code}")
        
        # Check if the content type is an image
        if 'image' not in response.headers['Content-Type']:
            raise ValueError("The fetched content is not a valid image format.")
        
        # Convert the response content to a PIL Image object
        image = Image.open(io.BytesIO(response.content))
        
        return image
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to fetch image: {e}")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")