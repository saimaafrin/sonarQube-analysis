import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2
import os
def task_func(file_path, onpick):
    """
    Draw the color histogram of an image in 3D and call a function when a data point is selected.

    Parameters:
    file_path (str): The path to the image file.
    onpick (function): The function to be called when a data point is picked.

    Returns:
    matplotlib.axes.Axes: The Axes object of the 3D plot.

    Raises:
    FileNotFoundError: If the image file does not exist.
    
    Requirements:
    - matplotlib
    - mpl_toolkits.mplot3d
    - numpy
    - cv2
    - os
    - tempfile
    
    Example:
    >>> def onpick(event):
    ...     ind = event.ind
    ...     print(f'You picked data point(s) {ind}')
    >>> np.random.seed(42)
    >>> dummy_img_path = 'image.jpg'
    >>> dummy_img = np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)
    >>> cv2.imwrite(dummy_img_path, dummy_img)
    True
    >>> ax = task_func('image.jpg', onpick)
    >>> os.remove(dummy_img_path)
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File {file_path} does not exist.')
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.reshape((img.shape[0] * img.shape[1], 3))
    img = img.astype(np.float64)
    img = img / 255.0
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue')
    ax.set_title('Color Histogram')
    ax.scatter(img[:, 0], img[:, 1], img[:, 2], c=img, cmap='viridis')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_zticks([0, 1])
    ax.grid(False)
    ax.set_xticklabels([0, 255])
    ax.set_yticklabels([0, 255])
    ax.set_zticklabels([0, 255])
    ax.xaxis.set_major_formatter(plt.NullFormatter())
    ax.yaxis.set_major_formatter(plt.NullFormatter())
    ax.zaxis.set_major_formatter(plt.NullFormatter())
    ax.xaxis.set_minor_formatter(plt.NullFormatter())
    ax.yaxis.set_minor_formatter(plt.NullFormatter())
    ax.zaxis.set_minor_formatter(plt.NullFormatter())
    ax.xaxis.set_minor_locator(plt.NullLocator())
    ax.yaxis.set_minor_locator(plt.NullLocator())
    ax.zaxis.set_minor_locator(plt.NullLocator())
    ax.xaxis.set_major_locator(plt.MultipleLocator(0.5))
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
    ax.zaxis.set_major_locator(plt.MultipleLocator(0.5))
    ax.xaxis.set_major_formatter(plt.NullFormatter())
    ax.yaxis.set_major_formatter(plt.NullFormatter())
    ax.zaxis.set_major_formatter(plt.NullFormatter())
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
    ax.zaxis.set_minor_locator(plt.MultipleLocator(0.1))
    ax.xaxis.set_minor_formatter(plt.NullFormatter())
    ax.yaxis.set_minor_formatter(plt.NullFormatter())
    ax.zaxis.set_minor_formatter(plt.NullFormatter())
    ax.set_facecolor((0.9, 0.9, 0.9))
    ax.set_axis_off()
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=30, azim=45)
    ax.set_pickradius(1)
    ax.pick_event = None
    ax.pick_event = ax.figure.canvas.mpl_connect('pick_event', onpick)
    return ax