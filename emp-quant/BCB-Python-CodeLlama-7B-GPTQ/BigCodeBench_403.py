from PIL import Image, ImageFilter
import cv2
import numpy as np
import os
def task_func(img_path, blur_radius=5):
    """
    Open an RGB image from a specific path, apply a blur filter, convert it to grayscale, and then display both the original and the edited images side by side.
    Returns a tuple containing two numpy arrays, the first representing the original image and the second representing the blurred and grayscaled image.
    Raises FileNotFoundError if the image file does not exist at the specified path.
    """
    # Check if the image file exists
    if not os.path.isfile(img_path):
        raise FileNotFoundError(f"Image file {img_path} does not exist.")

    # Open the image and convert it to grayscale
    img = Image.open(img_path)
    img_gray = img.convert("L")

    # Apply a blur filter to the grayscale image
    img_blur = img_gray.filter(ImageFilter.GaussianBlur(blur_radius))

    # Convert the blurred image to numpy array
    img_blur_np = np.array(img_blur)

    # Convert the original image to numpy array
    img_np = np.array(img)

    # Display both images side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.imshow(img_np, cmap="gray")
    ax2.imshow(img_blur_np, cmap="gray")
    plt.show()

    # Return the original and blurred images as numpy arrays
    return img_np, img_blur_np
img_path = "path/to/image.jpg"
blur_radius = 5