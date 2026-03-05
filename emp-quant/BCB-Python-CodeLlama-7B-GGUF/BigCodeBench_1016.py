
import requests
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def task_func(url: str) -> "matplotlib.axes._axes.Axes":
    try:
        response = requests.get(url)
        image = Image.open(response.content)
        image = image.convert("L")
        histogram = np.histogram(image, bins=256, range=(0, 256))
        ax = plt.axes()
        ax.bar(histogram[1][:-1], histogram[0], width=1, align="edge")
        ax.set_xlabel("Grayscale value")
        ax.set_ylabel("Frequency")
        ax.set_title("Grayscale histogram")
        return ax
    except ValueError as e:
        raise ValueError("Invalid URL or download error: " + str(e))
    except IOError as e:
        raise IOError("Error opening or processing downloaded image: " + str(e))