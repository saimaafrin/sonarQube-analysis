
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

def task_func(img_path, angle):
    # Check if the image file exists
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"The image file does not exist at the specified path: {img_path}")
    
    # Open the image
    original_img = Image.open(img_path)
    
    # Convert the image to a numpy array
    original_img_np = np.array(original_img)
    
    # Rotate the image
    rotated_img = original_img.rotate(angle, expand=True)
    
    # Convert the rotated image to a numpy array
    rotated_img_np = np.array(rotated_img)
    
    # Display both images side by side
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(original_img_np)
    axs[0].set_title('Original Image')
    axs[1].imshow(rotated_img_np)
    axs[1].set_title('Rotated Image')
    plt.show()
    
    # Return both images as numpy arrays
    return original_img_np, rotated_img_np