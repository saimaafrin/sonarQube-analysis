
import numpy as np
import cv2
import os

def task_func(image_path='image.jpg', threshold=128):
    # Check if the image file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError("Image file does not exist")

    # Read the image and convert it to grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Binarize the image using the given threshold
    binarized_image = np.where(image > threshold, 1, 0)

    # Return the original and binarized images as numpy arrays
    return (image, binarized_image)