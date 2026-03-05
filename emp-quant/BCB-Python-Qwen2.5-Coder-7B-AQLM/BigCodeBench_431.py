
import cv2
import os
import numpy as np

def task_func(image_file: str) -> np.ndarray:
    # Check if the image file exists
    if not os.path.exists(image_file):
        raise FileNotFoundError(f"The file {image_file} does not exist.")
    
    # Read the image in grayscale mode
    try:
        image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
    except Exception as e:
        raise ValueError(f"The file {image_file} is not a valid image.") from e
    
    # Check if the image is in grayscale
    if image is None:
        raise ValueError(f"The file {image_file} is not a valid grayscale image.")
    
    # Calculate the histogram of the image
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    
    # Convert the histogram to a numpy array
    histogram = np.squeeze(histogram)
    
    return histogram