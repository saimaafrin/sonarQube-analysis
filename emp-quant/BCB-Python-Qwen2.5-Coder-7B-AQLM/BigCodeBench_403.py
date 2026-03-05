
from PIL import Image, ImageFilter
import cv2
import numpy as np
import os

def task_func(img_path, blur_radius=5):
    try:
        # Open the image using PIL
        original_image = Image.open(img_path)
        
        # Convert the PIL image to a numpy array
        original_array = np.array(original_image)
        
        # Apply a blur filter using PIL
        blurred_image = original_image.filter(ImageFilter.GaussianBlur(blur_radius))
        
        # Convert the blurred PIL image to a numpy array
        blurred_array = np.array(blurred_image)
        
        # Convert the blurred image to grayscale using OpenCV
        gray_array = cv2.cvtColor(blurred_array, cv2.COLOR_RGB2GRAY)
        
        # Display both images side by side using PIL
        combined_image = Image.fromarray(np.hstack((original_array, gray_array)))
        combined_image.show()
        
        # Return the numpy arrays
        return (original_array, gray_array)
    
    except FileNotFoundError:
        raise FileNotFoundError("The image file does not exist at the specified path.")