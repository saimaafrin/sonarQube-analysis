
import cv2
import os
from matplotlib import pyplot as plt

def task_func(image_path='image.jpg', histogram_path='histogram.png'):
    # Read the image
    image = cv2.imread(image_path)

    # Create a histogram of the image pixel intensities
    histogram = cv2.calcHist([image], [0], [256], [0, 256])

    # Display the original image and its histogram
    plt.figure()
    plt.subplot(121)
    plt.imshow(image)
    plt.subplot(122)
    plt.imshow(histogram, cmap='gray')
    plt.show()

    # Save the histogram as a PNG file
    plt.savefig(histogram_path)

    # Return the histogram plot object
    return plt.gca()