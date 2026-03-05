import cv2
import matplotlib.pyplot as plt
def task_func(image_path, kernel_size):
    # Check if the kernel_size is a positive integer
    if not isinstance(kernel_size, int) or kernel_size <= 0:
        raise ValueError("kernel_size must be a positive integer")

    # Check if the image file exists
    if not cv2.imread(image_path):
        raise FileNotFoundError("The specified image file does not exist")

    # Read the image
    image = cv2.imread(image_path)

    # Apply a blur effect using the specified kernel size
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    # Create a figure with two subplots side by side
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Display the original image
    axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axs[0].set_title('Original Image')
    axs[0].axis('off')

    # Display the blurred image
    axs[1].imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
    axs[1].set_title('Blurred Image')
    axs[1].axis('off')

    # Return the blurred image and the two axes objects
    return blurred_image, axs