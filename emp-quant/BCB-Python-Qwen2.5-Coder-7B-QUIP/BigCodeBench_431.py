
import cv2
import os
import numpy as np

def task_func(image_file: str) -> np.ndarray:
    # Check if the image file exists
    if not os.path.exists(image_file):
        raise FileNotFoundError(f"The image file '{image_file}' does not exist.")
    
    # Load the image in grayscale
    image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
    
    # Check if the image is loaded correctly
    if image is None:
        raise ValueError(f"The image file '{image_file}' is not a valid image.")
    
    # Calculate the histogram of the image
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    
    # Normalize the histogram to get the frequency of each pixel value
    histogram = cv2.normalize(histogram, None, 0, 1, cv2.NORM_MINMAX)
    
    return histogram