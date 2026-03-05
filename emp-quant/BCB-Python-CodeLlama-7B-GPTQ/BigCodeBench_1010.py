import requests
from PIL import Image
import io
def task_func(url):
    """
    Fetches an image from a given URL and returns it as a PIL Image object.
    """
    try:
        response = requests.get(url, timeout=5)
        if response.status_code not in range(200, 299):
            raise ValueError(f"Invalid status code: {response.status_code}")
        image_data = response.content
        image_file = io.BytesIO(image_data)
        image = Image.open(image_file)
        return image
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error fetching image from URL: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid image format: {e}")