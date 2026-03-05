
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

def task_func(image, sigma=2):
    if sigma <= 0:
        raise ValueError("Sigma must be positive")
    if not isinstance(image, np.ndarray):
        raise TypeError("Input must be a numpy array")

    filtered_image = gaussian_filter(image, sigma)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.imshow(image, cmap='gray')
    ax1.set_title('Original')
    ax2.imshow(filtered_image, cmap='gray')
    ax2.set_title('Filtered')
    plt.show()

    return ax, filtered_image