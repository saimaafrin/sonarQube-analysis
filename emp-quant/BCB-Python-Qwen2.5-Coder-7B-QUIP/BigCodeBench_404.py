
import cv2
import numpy as np
import os

def task_func(img_path):
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"The image file at {img_path} does not exist.")
    
    # Open the RGB image
    img = cv2.imread(img_path)
    
    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Find contours
    contours, _ = cv2.findContours(gray_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Return the original image and contours
    return (img, contours)