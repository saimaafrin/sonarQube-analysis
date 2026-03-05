import numpy as np
import cv2
import os
def task_func(image_path='image.jpg', threshold=128):
    # Check if the image file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The image file {image_path} does not exist.")
    
    # Check if the threshold is an integer and within the valid range
    if not isinstance(threshold, int) or threshold < 0 or threshold > 255:
        raise ValueError("Threshold must be an integer between 0 and 255.")
    
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Binarize the image using the given threshold
    _, binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)
    
    # Return the original and binarized images as numpy arrays
    return gray_image, binary_image