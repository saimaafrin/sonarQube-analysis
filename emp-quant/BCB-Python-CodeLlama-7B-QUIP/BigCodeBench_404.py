
import cv2
import numpy as np
import os

def task_func(img_path):
    # Open the image file
    try:
        img = cv2.imread(img_path)
    except cv2.error:
        raise FileNotFoundError(f"Image file {img_path} does not exist")

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the contours
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return (img, contours)