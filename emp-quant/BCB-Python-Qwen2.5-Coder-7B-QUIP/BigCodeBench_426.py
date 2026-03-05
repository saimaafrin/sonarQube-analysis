
import numpy as np
import cv2
import os

def task_func(image_path='image.jpg', threshold=128):
    # Check if the image file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found at {image_path}")

    # Check if the threshold is an integer and within the valid range
    if not isinstance(threshold, int) or not (0 <= threshold <= 255):
        raise ValueError("Threshold must be an integer between 0 and 255")

    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image was read successfully
    if image is None:
        raise ValueError("Failed to read the image")

    # Binarize the image using the threshold
    _, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)

    # Return the original and binarized images as numpy arrays
    return image, binary_image