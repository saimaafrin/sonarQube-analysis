
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

def task_func(img_path, angle):
    # Check if the image file exists
    if not os.path.isfile(img_path):
        raise FileNotFoundError(f"Image file {img_path} does not exist")

    # Open the image and rotate it
    img = Image.open(img_path)
    rotated_img = img.rotate(angle, expand=True)

    # Convert the images to numpy arrays
    original_array = np.array(img)
    rotated_array = np.array(rotated_img)

    # Display the original and rotated images side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.imshow(original_array)
    ax2.imshow(rotated_array)
    plt.show()

    # Return the original and rotated images as numpy arrays
    return original_array, rotated_array