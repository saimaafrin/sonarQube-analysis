
import cv2
import numpy as np
import os

def task_func(img_path):
    # Check if the image file exists
    if not os.path.isfile(img_path):
        raise FileNotFoundError("Image file does not exist at the specified path")

    # Read the image and convert it to grayscale
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find contours in the grayscale image
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Return the original image and contours
    return img, contours

# Print the original image and contours
print(img)
print(contours)