
import numpy as np
import cv2
import os

def task_func(image_path='image.jpg', threshold=128):
    """
    Read an RGB image, convert it to grayscale, binarize it using a given threshold, and return both the original and binarized images as numpy arrays.

    Parameters:
    image_path (str): Path to the image file.
    threshold (int): Threshold value for binarization.

    Returns:
    tuple: A tuple containing two numpy arrays. The first array represents the original grayscale image,
    and the second array represents the binarized image.

    Raises:
    FileNotFoundError: If the image file does not exist at the specified path.
    ValueError: If the threshold is not an integer or not in the range 0-255.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file {image_path} does not exist.")
    if not isinstance(threshold, int) or (threshold < 0 or threshold > 255):
        raise ValueError(f"Threshold value {threshold} is not an integer or not in the range 0-255.")

    # Read the image
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Binarize the image
    _, binarized = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    # Return both the original and binarized images as numpy arrays
    return (gray, binarized)

try:
    original, binarized = task_func(image_path, threshold)
    print(f"Original image shape: {original.shape}")
    print(f"Binarized image shape: {binarized.shape}")
except FileNotFoundError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: {e}")