
from PIL import Image, ImageFilter
import cv2
import numpy as np
import os

def task_func(img_path, blur_radius=5):
    # Check if the image file exists
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"Image file does not exist at path: {img_path}")

    # Open the image and convert it to grayscale
    img = Image.open(img_path)
    img_gray = img.convert("L")

    # Apply a blur filter to the grayscale image
    img_blur = img_gray.filter(ImageFilter.GaussianBlur(blur_radius))

    # Convert the blurred image back to RGB
    img_blur_rgb = img_blur.convert("RGB")

    # Display both the original and blurred images side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
    ax1.imshow(img)
    ax2.imshow(img_blur_rgb)
    plt.show()

    # Return the original and blurred images as numpy arrays
    return np.array(img), np.array(img_blur_rgb)