
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

def task_func(img_path, angle):
    # Check if the image file exists
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"Image file not found at path: {img_path}")

    # Open the image
    original_img = Image.open(img_path)
    original_img_array = np.array(original_img)

    # Rotate the image
    rotated_img = original_img.rotate(angle, expand=True)
    rotated_img_array = np.array(rotated_img)

    # Display both images side by side
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(original_img_array, cmap='gray')
    axs[0].set_title('Original Image')
    axs[1].imshow(rotated_img_array, cmap='gray')
    axs[1].set_title('Rotated Image')
    plt.show()

    return original_img_array, rotated_img_array