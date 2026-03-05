
from PIL import Image, ImageFilter
import cv2
import numpy as np
import os

def task_func(img_path, blur_radius=5):
    # Load the image
    img = Image.open(img_path)

    # Apply the blur filter
    img_blurred = img.filter(ImageFilter.BLUR)

    # Convert to grayscale
    img_gray = img_blurred.convert('L')

    # Display the original and blurred images side by side
    img_gray_array = np.array(img_gray)
    img_blurred_array = np.array(img_blurred)
    img_side_by_side = np.concatenate((img_gray_array, img_blurred_array), axis=1)
    cv2.imshow("Side by side", img_side_by_side)

    # Return the original and blurred images as numpy arrays
    return np.array(img), np.array(img_blurred)