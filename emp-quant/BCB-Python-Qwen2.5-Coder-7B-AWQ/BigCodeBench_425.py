import cv2
import os
from matplotlib import pyplot as plt
def task_func(image_path='image.jpg', histogram_path='histogram.png'):
    # Check if the image file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The image file {image_path} does not exist.")

    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image was successfully read
    if image is None:
        raise ValueError(f"Failed to read the image file {image_path}.")

    # Create a histogram of the image pixel intensities
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Save the histogram as a PNG file
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.savefig(histogram_path)

    # Display the original image and its histogram
    plt.figure()
    plt.subplot(121), plt.imshow(image, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.plot(hist)
    plt.title('Histogram'), plt.xlim([0, 256])
    plt.show()

    # Return the histogram plot object
    return plt.gca()