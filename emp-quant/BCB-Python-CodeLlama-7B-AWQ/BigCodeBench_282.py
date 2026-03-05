import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2
import os
def task_func(file_path, onpick):
    """
    Draw the color histogram of an image in 3D and call a function when a data point is selected.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")

    image = cv2.imread(file_path)
    hist = cv2.calcHist([image], [0, 1, 2], None, [256], [0, 256, 0, 256, 0, 256])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.bar3d(hist[:, 0], hist[:, 1], hist[:, 2], hist[:, 0], hist[:, 1], hist[:, 2], color='b')

    def onpick(event):
        if event.artist is not None:
            print(f"Selected data point: {event.artist.get_xdata()}, {event.artist.get_ydata()}, {event.artist.get_zdata()}")

    fig.canvas.mpl_connect('pick_event', onpick)

    return ax
file_path = "path/to/image.jpg"
onpick = lambda event: print(f"Selected data point: {event.artist.get_xdata()}, {event.artist.get_ydata()}, {event.artist.get_zdata()}")