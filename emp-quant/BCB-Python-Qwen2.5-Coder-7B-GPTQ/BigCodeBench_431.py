import cv2
import os
import numpy as np
def task_func(image_file: str) -> np.ndarray:
    # Check if the image file exists
    if not os.path.exists(image_file):
        raise FileNotFoundError(f"The file {image_file} does not exist.")
    
    # Read the image using OpenCV
    image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
    
    # Check if the image is loaded correctly
    if image is None:
        raise ValueError(f"The file {image_file} is not a valid image.")
    
    # Flatten the image to a 1D array
    flattened_image = image.flatten()
    
    # Create a histogram with 256 bins
    histogram = np.zeros(256, dtype=int)
    
    # Count the frequency of each pixel value
    for pixel_value in flattened_image:
        histogram[pixel_value] += 1
    
    return histogram