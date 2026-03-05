
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2
import os

def task_func(file_path, onpick):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Image file {file_path} does not exist.")

    image = cv2.imread(file_path)
    height, width, _ = image.shape

    x = np.arange(0, width)
    y = np.arange(0, height)
    z = image.reshape(height * width)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')

    def onpick(event):
        if event.artist == ax.patches[0]:
            x, y = event.mouseevent.xdata, event.mouseevent.ydata
            z = image[y, x]
            print(f"Selected point: ({x}, {y}) with value {z}")

    fig.canvas.mpl_connect('pick_event', onpick)

    plt.show()