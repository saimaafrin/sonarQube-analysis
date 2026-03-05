
from PIL import Image, ImageFilter
import cv2
import numpy as np
import os

def task_func(img_path, blur_radius=5):
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"Image file not found at path: {img_path}")

    # Open the image using PIL
    img = Image.open(img_path)

    # Apply a blur filter to the image
    img_blurred = img.filter(ImageFilter.GaussianBlur(blur_radius))

    # Convert the image to grayscale
    img_gray = cv2.cvtColor(np.array(img_blurred), cv2.COLOR_BGR2GRAY)

    # Display both the original and blurred images side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.imshow(img)
    ax2.imshow(img_gray)
    plt.show()

    # Return the original and blurred images as numpy arrays
    return np.array(img), np.array(img_gray)