
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

def task_func(image, sigma=2):
    # Check if sigma is non-positive
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    
    # Check if input is a numpy array
    if not isinstance(image, np.ndarray):
        raise TypeError("input must be a numpy array")
    
    # Apply Gaussian filter
    filtered_image = gaussian_filter(image, sigma=sigma)
    
    # Create a figure with two subplots
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    
    # Plot the original image
    ax[0].imshow(image, cmap='gray')
    ax[0].set_title('Original')
    
    # Plot the filtered image
    ax[1].imshow(filtered_image, cmap='gray')
    ax[1].set_title('Filtered')
    
    # Return the axes object and the filtered image
    return ax, filtered_image