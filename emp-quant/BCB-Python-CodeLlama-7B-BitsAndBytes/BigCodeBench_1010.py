
import requests
from PIL import Image
import io

def task_func(url):
    # Set the timeout for the HTTP request to 5 seconds
    timeout = 5

    # Send a GET request to the URL
    response = requests.get(url, timeout=timeout)

    # Check if the response is a successful HTTP status code (200-299)
    if response.status_code not in range(200, 300):
        raise ValueError("Invalid URL or unable to reach the server within the timeout period")

    # Check if the content fetched from the URL is a valid image format that can be handled by PIL
    if not response.headers["Content-Type"].startswith("image"):
        raise ValueError("The content fetched from the URL is not a valid image format")

    # Convert the response content to a PIL Image object
    image = Image.open(io.BytesIO(response.content))

    # Return the PIL Image object
    return image