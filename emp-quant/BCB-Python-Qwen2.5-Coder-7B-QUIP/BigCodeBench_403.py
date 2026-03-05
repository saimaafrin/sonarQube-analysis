
from PIL import Image, ImageFilter
import cv2
import numpy as np
import os

def task_func(img_path, blur_radius=5):
    # Check if the image file exists
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"Image file not found at path: {img_path}")

    # Open the image using PIL
    original_img = Image.open(img_path)

    # Apply a blur filter
    blurred_img = original_img.filter(ImageFilter.BLUR)

    # Convert the original image to grayscale
    grayscale_img = original_img.convert('L')

    # Convert images to numpy arrays
    original_img_array = np.array(original_img)
    blurred_img_array = np.array(blurred_img)
    grayscale_img_array = np.array(grayscale_img)

    # Display the images side by side
    combined_img = cv2.resize(np.hstack((original_img_array, blurred_img_array, grayscale_img_array)), None, interpolation=cv2.INTER_AREA)
    cv2.imshow('Original, Blurred, Grayscale', combined_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Return the numpy arrays
    return original_img_array, blurred_img_array