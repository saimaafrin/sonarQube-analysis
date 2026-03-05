
import cv2
import os
from matplotlib import pyplot as plt

def task_func(image_path='image.jpg', histogram_path='histogram.png'):
    # Check if the image file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found at path: {image_path}")

    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Calculate the histogram
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Normalize the histogram
    hist = cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)

    # Create a figure and axes for displaying the image and histogram
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Display the image
    axs[0].imshow(image, cmap='gray')
    axs[0].set_title('Image')
    axs[0].axis('off')

    # Display the histogram
    axs[1].plot(hist, 'r')
    axs[1].set_title('Histogram')
    axs[1].set_xlabel('Bins')
    axs[1].set_ylabel('Frequency')

    # Save the histogram as a PNG file
    plt.savefig(histogram_path, dpi=300)

    # Return the histogram plot object
    return axs[1]