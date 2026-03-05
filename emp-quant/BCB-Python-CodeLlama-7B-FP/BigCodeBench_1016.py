import requests
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
def task_func(url: str) -> "matplotlib.axes._axes.Axes":
    """
    Downloads an image from the specified URL, converts it to grayscale, and generates a histogram of its grayscale values.
    The function should raise the exception for:
        ValueError: If the URL is invalid or if there's an error downloading the image. Error message will specify the download issue.
        IOError: If there's an error in opening or processing the downloaded image. Error message will specify the processing issue.
    The function should output with:
        matplotlib.axes._axes.Axes: The Axes object of the generated histogram.
    """
    try:
        # Download the image
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError(f"Error downloading image from {url}: {response.status_code}")
        image_data = response.content

        # Convert the image to grayscale
        image = Image.open(io.BytesIO(image_data))
        image = image.convert("L")

        # Generate a histogram of the grayscale values
        histogram = np.histogram(image.getdata(), bins=256, range=(0, 256))

        # Plot the histogram
        fig, ax = plt.subplots()
        ax.bar(histogram[1], histogram[0], width=1, align="center")
        ax.set_xlabel("Grayscale value")
        ax.set_ylabel("Frequency")
        ax.set_title("Grayscale histogram")
        return ax
    except (ValueError, IOError) as e:
        raise e