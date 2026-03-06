from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
def task_func(img_path, angle):
    """
    Open an image, rotate it around a certain angle, and then display both the original and the rotated images side by side. 
    Additionally, return both images as numpy arrays.

    Parameters:
    img_path (str): The path of the image file.
    angle (float): The angle to rotate the image (in degrees).

    Returns:
    tuple: A tuple containing two numpy arrays, the first representing the original image and 
           the second representing the rotated image. Expands the rotated image to make it large enough to hold the entire rotated image.

    Raises:
    FileNotFoundError: If the image file does not exist at the specified path.

    Requirements:
    - PIL
    - matplotlib
    - numpy
    - os

    Example:
    >>> img_path = 'sample.png'
    >>> create_dummy_image(image_path=img_path)
    >>> original_img_array, rotated_img_array = task_func(img_path, 45)
    >>> os.remove(img_path)
    """
    # Open the image
    img = Image.open(img_path)

    # Rotate the image
    rotated_img = img.rotate(angle)

    # Convert the image to a numpy array
    original_img_array = np.array(img)
    rotated_img_array = np.array(rotated_img)

    # Expand the rotated image to make it large enough to hold the entire rotated image
    rotated_img_array = np.pad(rotated_img_array, ((0, original_img_array.shape[0] - rotated_img_array.shape[0]), (0, original_img_array.shape[1] - rotated_img_array.shape[1]), (0, 0)), 'constant')

    # Display the original and rotated images side by side
    plt.figure(figsize=(10, 10))
    plt.subplot(1, 2, 1)
    plt.imshow(original_img_array)
    plt.title('Original Image')
    plt.subplot(1, 2, 2)
    plt.imshow(rotated_img_array)
    plt.title('Rotated Image')
    plt.show()

    return original_img_array, rotated_img_array