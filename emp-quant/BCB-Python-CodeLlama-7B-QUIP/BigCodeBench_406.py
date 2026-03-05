
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

def task_func(img_path, angle):
    # Load the image
    try:
        img = Image.open(img_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Image file {img_path} does not exist")

    # Rotate the image
    rotated_img = img.rotate(angle, expand=1)

    # Convert the image to numpy array
    img_array = np.array(img)
    rotated_img_array = np.array(rotated_img)

    # Display the original and rotated images side by side
    fig, ax = plt.subplots(nrows=1, ncols=2)
    ax[0].imshow(img_array)
    ax[1].imshow(rotated_img_array)
    plt.show()

    # Return the original and rotated images as numpy arrays
    return img_array, rotated_img_array