
import cv2
import os
import numpy as np

def task_func(image_file: str) -> np.ndarray:
    # Check if the image file exists
    if not os.path.isfile(image_file):
        raise FileNotFoundError("Image file does not exist")

    # Load the image using OpenCV
    image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

    # Check if the image is valid
    if image is None:
        raise ValueError("Image is not a valid image")

    # Create a histogram of the image
    histogram = np.histogram(image, bins=256)

    # Return the histogram
    return histogram