import cv2
import os
from matplotlib import pyplot as plt
def task_func(image_path='image.jpg', histogram_path='histogram.png'):
    """
    Read an image, create a histogram of the image pixel intensities, save the histogram as a PNG file, and return the histogram plot object.
    The function also displays the original image and its histogram.
    The limit to the size of the image depends on the hardware capabilities of the system you are working on.
    A possible size of an image is 20x20.
    The function should raise the exception for:
        FileNotFoundError: If the image file does not exist at the specified path.
    The function should output with:
        matplotlib.axes.Axes: The Axes object of the histogram plot.
    """
    # Check if the image file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file {image_path} does not exist")

    # Read the image
    image = cv2.imread(image_path)

    # Create a histogram of the image pixel intensities
    hist, bins = np.histogram(image.ravel(), bins='auto')

    # Normalize the histogram
    hist = hist / hist.max()

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], hist, width=bins[1] - bins[0])
    ax.set_xlabel('Pixel intensity')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of image pixel intensities')

    # Display the original image and its histogram
    fig.tight_layout()
    fig.show()

    # Save the histogram as a PNG file
    fig.savefig(histogram_path)

    # Return the histogram plot object
    return ax
image_path = 'image.jpg'
histogram_path = 'histogram.png'