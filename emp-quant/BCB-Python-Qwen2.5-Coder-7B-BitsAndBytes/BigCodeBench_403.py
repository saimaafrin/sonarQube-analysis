
from PIL import Image, ImageFilter
import cv2
import numpy as np
import os

def task_func(img_path, blur_radius=5):
    # Check if the image file exists
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"The image file {img_path} does not exist.")
    
    # Open the image using PIL
    original_image = Image.open(img_path)
    
    # Convert the PIL image to a NumPy array
    original_array = np.array(original_image)
    
    # Apply a Gaussian blur filter
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(blur_radius))
    
    # Convert the blurred PIL image to a NumPy array
    blurred_array = np.array(blurred_image)
    
    # Convert the blurred image to grayscale
    gray_blurred_array = cv2.cvtColor(blurred_array, cv2.COLOR_RGB2GRAY)
    
    # Display both images side by side
    combined_image = np.hstack((original_array, gray_blurred_array))
    cv2.imshow('Original vs Blurred Grayscale', combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return (original_array, gray_blurred_array)