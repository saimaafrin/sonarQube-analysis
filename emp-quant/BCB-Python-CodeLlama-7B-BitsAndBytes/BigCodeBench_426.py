
import numpy as np
import cv2
import os

def task_func(image_path='image.jpg', threshold=128):
    # Check if the image file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError("Image file does not exist at the specified path")

    # Check if the threshold is an integer and in the range 0-255
    if not isinstance(threshold, int) or threshold < 0 or threshold > 255:
        raise ValueError("Threshold value must be an integer in the range 0-255")

    # Read the image and convert it to grayscale
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Binarize the image using the given threshold
    ret, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    # Save the binarized image as 'binary_image.jpg'
    cv2.imwrite('binary_image.jpg', binary)

    # Return the original and binarized images as a tuple
    return (image, binary)

# Call the function and print the output
result = task_func(image_path, threshold)
print(result)