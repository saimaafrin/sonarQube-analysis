import cv2
import os
import numpy as np
def task_func(image_file: str) -> np.ndarray:
    # Check if the image file exists
    if not os.path.exists(image_file):
        raise FileNotFoundError(f"The specified image file '{image_file}' does not exist.")
    
    # Read the image
    image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
    
    # Check if the image is valid
    if image is None:
        raise ValueError(f"The specified image file '{image_file}' is not a valid image.")
    
    # Calculate the histogram
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    
    # Flatten the histogram to get a 1D array
    histogram = histogram.flatten()
    
    return histogram