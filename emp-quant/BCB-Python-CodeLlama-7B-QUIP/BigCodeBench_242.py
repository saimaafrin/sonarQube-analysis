
import cv2
import matplotlib.pyplot as plt

def task_func(image_path, kernel_size):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image exists
    if not image.any():
        raise FileNotFoundError("Image file does not exist")

    # Check if the kernel size is a positive integer
    if kernel_size <= 0:
        raise ValueError("Kernel size must be a positive integer")

    # Apply the blur effect
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    # Visualize the original and blurred images side by side
    fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True)
    ax[0].imshow(image)
    ax[1].imshow(blurred_image)
    ax[0].set_title("Original Image")
    ax[1].set_title("Blurred Image")
    plt.show()

    return (blurred_image, ax[0], ax[1])