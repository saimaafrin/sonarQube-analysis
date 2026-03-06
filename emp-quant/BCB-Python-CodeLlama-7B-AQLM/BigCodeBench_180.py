from PIL import Image
import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt
import os
def task_func(img_path, scale_factors=[0.5, 0.75, 1.5, 2.0]):
    """
    Open an image file and scale it by different scaling factors.
    Display each scaled image using matplotlib and return the scaled images with their Axes.

    Parameters:
    img_path (str): Path to the image file.
    scale_factors (list): List of scaling factors to apply. Default is [0.5, 0.75, 1.5, 2.0].

    Returns:
    list of tuples: Each tuple contains (matplotlib.axes.Axes, numpy.ndarray) representing the Axes and the pixel values of the scaled image.

    Raises:
    FileNotFoundError: If the image file cannot be found.

    Requirements:
    - PIL
    - numpy
    - scikit-image
    - matplotlib.pyplot
    - os

    Example:
    >>> dummy_img_path = "sample.png"
    >>> Image.fromarray(np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)).save(dummy_img_path)
    >>> result = task_func('sample.png')
    >>> os.remove(dummy_img_path)
    >>> for ax, img in result:
    ...     print(ax.get_title(), img.shape)
    Scale factor: 0.5 (10, 10, 3)
    Scale factor: 0.75 (15, 15, 3)
    Scale factor: 1.5 (30, 30, 3)
    Scale factor: 2.0 (40, 40, 3)
    """
    try:
        img = Image.open(img_path)
    except FileNotFoundError:
        raise FileNotFoundError("Image file not found.")

    fig, axes = plt.subplots(nrows=len(scale_factors), ncols=1, figsize=(10, 10))
    for i, scale_factor in enumerate(scale_factors):
        axes[i].set_title(f"Scale factor: {scale_factor}")
        axes[i].imshow(np.array(img))
        axes[i].axis("off")
        axes[i].set_xticklabels([])
        axes[i].set_yticklabels([])
        axes[i].set_aspect("equal")
        axes[i].set_xlim(0, axes[i].get_xlim()[1])
        axes[i].set_ylim(0, axes[i].get_ylim()[1])
        axes[i].set_xlabel(f"{img.width} x {img.height}")
        axes[i].set_ylabel(f"{img.width} x {img.height}")
        axes[i].set_title(f"Scale factor: {scale_factor}")
        axes[i].set_xlabel(f"{img.width} x {img.height}")
        axes[i].set_ylabel(f"{img.width} x {img.height}")
        axes[i].set_aspect("equal")
        axes[i].set_xticklabels([])
        axes[i].set_yticklabels([])
        axes[i].set_xlim(0, axes[i].get_xlim()[1])
        axes[i].set_ylim(0, axes[i].get_ylim()[1])
        axes[i].set_xlabel(f"{img.width} x {img.height}")
        axes[i].set_ylabel(f"{img.width} x {img.height}")
        axes[i].set_aspect("equal")
        axes[i].set_xticklabels([])
        axes[i].set_yticklabels([])
        axes[i].set_xlim(0, axes[i].get_xlim()[1])
        axes[i].set_ylim(0, axes[i].get_ylim()[1])
        axes[i].set_xlabel(f"{img.width} x {img.height}")
        axes[i].set_ylabel(f"{img.width} x {img.height}")
        axes[i].set_aspect("equal")
        axes[i].set_xticklabels([])
        axes[i].set_yticklabels([])
        axes[i].set_xlim(0, axes[i].get_xlim()[1])
        axes[i].set_ylim(0, axes[i].get_ylim()[1])
        axes[i].set_xlabel(f"{img.width} x {img.height}")
        axes[i].set_ylabel(f"{img.width} x {img.height}")
        axes[i].set_aspect("equal")
        axes[i].set_xticklabels([])
        axes[i].set_yticklabels([])
        axes[i].set_xlim(0, axes[i].get_xlim()[1])
        axes[i].set_ylim(0, axes[i].get_ylim()[1])
        axes[i].set_xlabel(f"{img.width} x {img.height}")
        axes[i].set_ylabel(f"{img.width} x {img.height}")
        axes[i].set_aspect("equal")
        axes[i].set_xticklabels([])
        axes[i].set_yticklabels([])
        axes[i].set_xlim(0, axes[i].get_xlim()[1])
        axes[i].set_ylim(0, axes[i].get_ylim()[1])
        axes[i].set_xlabel(f"{img.width} x {img.height}")
        axes[i].set_ylabel(f"{img.width} x {img.height}")
        axes[i].set_aspect("equal")
        axes[i].set_xticklabels([])
        axes[i].set_yticklabels([])
        axes[i].set_xlim(0, axes[i].get_xlim()[1])
        axes[i].set_ylim(0, axes[i].get_ylim()[1])
        axes[i].set_xlabel(f"{img.width} x {img.height}")
        axes[i].set_ylabel(f"{img.width} x {img.height}")
        axes[i].set_aspect("equal")
        axes[i].set_xticklabels([])
        axes[i].set_yticklabels([])
        axes[i].set_xlim(0, axes[i].get_xlim()[1])
        axes[i].set_ylim(0, axes[i].get_ylim()[1])
        axes[i].set_xlabel(f"{img.width} x {img.height}")
        axes[i].set_