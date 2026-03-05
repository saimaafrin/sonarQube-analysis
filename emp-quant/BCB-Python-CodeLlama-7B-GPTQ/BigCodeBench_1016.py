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
    # Download the image
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error downloading image: {e}")

    # Convert the image to grayscale
    try:
        image = Image.open(response.content)
        image = image.convert("L")
    except IOError as e:
        raise ValueError(f"Error opening or processing image: {e}")

    # Generate the histogram
    hist, bins = np.histogram(image, bins=256, density=True)

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.plot(bins[:-1], hist, color="blue")
    ax.set_xlabel("Grayscale value")
    ax.set_ylabel("Frequency")
    ax.set_title("Grayscale Histogram")

    return ax
url = "https://www.example.com/image.jpg"