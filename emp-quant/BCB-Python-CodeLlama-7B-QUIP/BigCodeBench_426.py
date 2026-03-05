
import numpy as np
import cv2
import os

def task_func(image_path='image.jpg', threshold=128):
    # Check if the image file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError("Image file does not exist")

    # Read the image and convert it to grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the threshold is an integer and in the range 0-255
    if not isinstance(threshold, int) or threshold < 0 or threshold > 255:
        raise ValueError("Threshold must be an integer and in the range 0-255")

    # Binarize the image using the threshold
    binary_image = np.where(image > threshold, 1, 0)

    # Save the binarized image
    cv2.imwrite('binary_image.jpg', binary_image)

    # Return the original and binarized images
    return image, binary_image