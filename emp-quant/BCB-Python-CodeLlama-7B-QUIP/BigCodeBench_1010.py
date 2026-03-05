
import requests
from PIL import Image
import io

def task_func(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code >= 200 and response.status_code < 300:
            image_stream = io.BytesIO(response.content)
            image = Image.open(image_stream)
            return image
        else:
            raise ValueError("Invalid response from server")
    except requests.exceptions.Timeout:
        raise ValueError("Timeout when fetching image")
    except requests.exceptions.HTTPError:
        raise ValueError("Invalid HTTP status code")
    except ValueError:
        raise ValueError("Invalid image format")