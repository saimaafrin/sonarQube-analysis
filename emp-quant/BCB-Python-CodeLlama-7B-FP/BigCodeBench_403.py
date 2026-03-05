from PIL import Image, ImageFilter
import cv2
import numpy as np
import os
def task_func(img_path, blur_radius=5):
    """
    Open an RGB image from a specific path, apply a blur filter, convert it to grayscale, and then display both the original and the edited images side by side. Returns numpy arrays representing both the original and the processed images.
    """
    # Check if the image file exists
    if not os.path.isfile(img_path):
        raise FileNotFoundError(f"Image file {img_path} does not exist")

    # Open the image and convert it to grayscale
    img = Image.open(img_path)
    img_gray = img.convert("L")

    # Apply a blur filter to the grayscale image
    img_blur = img_gray.filter(ImageFilter.GaussianBlur(blur_radius))

    # Convert the blurred image to numpy array
    img_blur_array = np.array(img_blur)

    # Convert the original image to numpy array
    img_array = np.array(img)

    # Display both images side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.imshow(img_array)
    ax2.imshow(img_blur_array)
    plt.show()

    # Return the original and blurred images as numpy arrays
    return img_array, img_blur_array
img_path = "path/to/image.jpg"
blur_radius = 5