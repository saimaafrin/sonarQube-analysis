from PIL import Image, ImageFilter
import cv2
import numpy as np
import os
def task_func(img_path, blur_radius=5):
    # Check if the image file exists
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"The image file does not exist at the specified path: {img_path}")
    
    # Open the RGB image
    original_image = Image.open(img_path)
    
    # Apply a blur filter
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(blur_radius))
    
    # Convert the blurred image to grayscale
    grayscale_image = blurred_image.convert('L')
    
    # Convert images to numpy arrays
    original_array = np.array(original_image)
    grayscale_array = np.array(grayscale_image)
    
    # Display both images side by side
    combined_image = np.hstack((original_array, grayscale_array))
    cv2.imshow('Original and Grayscale', combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Return the numpy arrays
    return original_array, grayscale_array