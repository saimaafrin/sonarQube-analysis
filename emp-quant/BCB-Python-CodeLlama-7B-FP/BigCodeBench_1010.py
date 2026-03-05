import requests
from PIL import Image
import io
def task_func(url):
    """
    Fetches an image from a given URL and returns it as a PIL Image object.

    Args:
        url (str): The URL of the image to fetch.

    Returns:
        PIL.Image.Image: A PIL Image object representing the downloaded image.

    Raises:
        ValueError: This exception is raised in the following scenarios:
            - The URL is invalid or cannot be reached within the timeout period (5 seconds).
            - The response from the server is not a successful HTTP status code (i.e., not in the range 200-299).
            - The content fetched from the URL is not a valid image format that can be handled by PIL.
    """
    try:
        response = requests.get(url, timeout=5)
        if response.status_code not in range(200, 299):
            raise ValueError(f"Invalid response status code: {response.status_code}")
        image_data = response.content
        image = Image.open(io.BytesIO(image_data))
        return image
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error fetching image from URL: {url}") from e