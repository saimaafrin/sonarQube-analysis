
import cv2
import matplotlib.pyplot as plt

def task_func(image_path, kernel_size):
    # Check if the image file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file {image_path} does not exist")

    # Check if kernel_size is a positive integer
    if not isinstance(kernel_size, int) or kernel_size <= 0:
        raise ValueError(f"Kernel size must be a positive integer, but got {kernel_size}")

    # Load the image and convert it to grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply the blur effect to the image
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    # Create two matplotlib figures and axes objects
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))

    # Plot the original and blurred images
    ax1.imshow(image, cmap="gray")
    ax1.set_title("Original Image")
    ax2.imshow(blurred_image, cmap="gray")
    ax2.set_title("Blurred Image")

    # Return the blurred image and the matplotlib axes objects
    return blurred_image, ax1, ax2

# Show the plots
plt.show()