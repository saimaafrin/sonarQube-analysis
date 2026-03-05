
import numpy as np
import cv2
import os

def task_func(image_path='image.jpg', threshold=128):
    # Check if the threshold is a valid integer
    if not isinstance(threshold, int):
        raise ValueError("Threshold must be an integer.")
    
    # Check if the threshold is within the valid range
    if threshold < 0 or threshold > 255:
        raise ValueError("Threshold must be in the range 0-255.")
    
    # Check if the image file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The image file '{image_path}' does not exist.")
    
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Binarize the image using the given threshold
    _, binarized_image = cv2.threshold(grayscale_image, threshold, 255, cv2.THRESH_BINARY)
    
    # Return the original and binarized images as numpy arrays
    return grayscale_image, binarized_image