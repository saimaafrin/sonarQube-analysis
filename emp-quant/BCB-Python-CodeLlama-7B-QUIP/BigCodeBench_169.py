
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

def task_func(image, sigma=2):
    if sigma <= 0:
        raise ValueError("Sigma must be positive")
    if not isinstance(image, np.ndarray):
        raise TypeError("Input must be a numpy array")
    filtered_image = gaussian_filter(image, sigma)
    fig, ax = plt.subplots(nrows=2, ncols=1)
    ax[0].imshow(image)
    ax[0].set_title("Original")
    ax[1].imshow(filtered_image)
    ax[1].set_title("Filtered")
    return ax, filtered_image