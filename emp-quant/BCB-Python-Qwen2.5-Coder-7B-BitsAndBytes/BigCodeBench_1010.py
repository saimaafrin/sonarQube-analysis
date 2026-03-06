
import requests
from PIL import Image
import io

def task_func(url):
    try:
        # Set a timeout of 5 seconds for the HTTP request
        response = requests.get(url, timeout=5)
        
        # Check if the response status code is successful (200-299)
        if not 200 <= response.status_code < 300:
            raise ValueError("HTTP response was not successful.")
        
        # Check if the content type indicates an image
        if 'image' not in response.headers['Content-Type']:
            raise ValueError("The fetched content is not a valid image format.")
        
        # Convert the binary data to a PIL Image object
        image = Image.open(io.BytesIO(response.content))
        
        return image
    
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to fetch the image: {e}")
    
    except KeyError:
        raise ValueError("Content-Type header not found in the response.")
    
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")