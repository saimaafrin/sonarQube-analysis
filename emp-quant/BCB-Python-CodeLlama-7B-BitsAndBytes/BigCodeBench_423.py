
import numpy as np
import cv2
import os

def task_func(image_path='image.jpg', threshold=128):
    # Check if the image file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file {image_path} does not exist")

    # Check if the threshold is an integer and in the range 0-255
    if not isinstance(threshold, int) or threshold < 0 or threshold > 255:
        raise ValueError(f"Threshold value {threshold} is not an integer or not in the range 0-255")

    # Read the image and convert it to grayscale
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Binarize the image using the given threshold
    _, binarized = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    # Return both the original and binarized images as numpy arrays
    return np.array(image), np.array(binarized)