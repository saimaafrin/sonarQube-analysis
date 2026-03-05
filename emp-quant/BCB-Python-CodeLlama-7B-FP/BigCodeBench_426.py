import numpy as np
import cv2
import os
def task_func(image_path='image.jpg', threshold=128):
    """
    Read an image, convert it to grayscale, binarize it using a given threshold, and save it as 'binary_image.jpg'.
    The function returns numpy arrays of the original and binarized images, and ensures that the threshold value is valid.
    The function should raise the exception for:
        FileNotFoundError: If the image file does not exist at the specified path.
        ValueError: If the threshold is not an integer or not in the range 0-255.
    The function should output with:
        tuple: A tuple containing two numpy arrays; the first is the original grayscale image, the second is the binarized image.
    """
    # Check if the image file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file '{image_path}' does not exist.")

    # Check if the threshold is an integer and in the range 0-255
    if not isinstance(threshold, int) or (threshold < 0 or threshold > 255):
        raise ValueError(f"Threshold value '{threshold}' is not an integer or not in the range 0-255.")

    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Binarize the image using the given threshold
    ret, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    # Save the binarized image
    cv2.imwrite('binary_image.jpg', binary)

    # Return the original and binarized images as numpy arrays
    return image, binary
image_path = 'image.jpg'
threshold = 128