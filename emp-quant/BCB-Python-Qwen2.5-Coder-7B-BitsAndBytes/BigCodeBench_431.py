
import cv2
import os
import numpy as np

def task_func(image_file: str) -> np.ndarray:
    # Check if the image file exists
    if not os.path.exists(image_file):
        raise FileNotFoundError(f"The file {image_file} does not exist.")
    
    try:
        # Read the image in grayscale mode
        image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
        
        # Check if the image was successfully read
        if image is None:
            raise ValueError(f"The file {image_file} is not a valid image.")
        
        # Calculate the histogram of the image
        histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
        
        # Convert the histogram to a 1D numpy array
        histogram_array = histogram.flatten()
        
        return histogram_array
    
    except Exception as e:
        raise ValueError(f"An error occurred while processing the image: {e}")