import numpy as np
import cv2
import os
def task_func(image_path='image.jpg', threshold=128):
    """
    Read an RGB image, convert it to grayscale, binarize it using a given threshold, and return both the original and binarized images as numpy arrays.
    The function checks for the existence of the image file and validates the threshold value.
    The function should raise the exception for:
        FileNotFoundError: If the image file does not exist at the specified path.
        ValueError: If the threshold is not an integer or not in the range 0-255.
    The function should output with:
        tuple: A tuple containing two numpy arrays. The first array represents the original grayscale image,
        and the second array represents the binarized image.
    """
    # Check if the image file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file {image_path} does not exist")

    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Binarize the image using the given threshold
    ret, binarized = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    # Return the original and binarized images as numpy arrays
    return (gray, binarized)
image_path = 'image.jpg'
threshold = 128