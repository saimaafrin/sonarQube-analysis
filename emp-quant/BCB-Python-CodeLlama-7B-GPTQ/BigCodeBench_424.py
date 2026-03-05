import cv2
import numpy as np
import os
from sklearn.cluster import KMeans
def task_func(image_path='image.jpg', n_clusters=3, random_seed=42):
    """
    Reads an RGB image, applies K-means clustering to segment the image into 'n_clusters' regions, and saves each region as a separate image.
    The function returns numpy arrays of the original and segmented images.
    """
    # Check if the image file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file '{image_path}' does not exist.")

    # Check if 'n_clusters' is a positive integer
    if not isinstance(n_clusters, int) or n_clusters < 1:
        raise ValueError(f"'n_clusters' must be a positive integer, but got {n_clusters}.")

    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Extract the Hue and Saturation channels
    hue = hsv[:, :, 0]
    sat = hsv[:, :, 1]

    # Flatten the Hue and Saturation channels into a single array
    hue_sat = np.concatenate((hue.flatten(), sat.flatten()), axis=0)

    # Perform K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_seed)
    kmeans.fit(hue_sat)

    # Get the cluster centroids
    centroids = kmeans.cluster_centers_

    # Create a new image with the same shape as the original image
    segmented_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

    # Assign each pixel to the corresponding cluster
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Get the Hue and Saturation values for the current pixel
            hue_val = hue[i, j]
            sat_val = sat[i, j]

            # Find the cluster that the pixel belongs to
            cluster_idx = np.argmin(np.linalg.norm(centroids - np.array([hue_val, sat_val]), axis=1))

            # Assign the pixel to the corresponding cluster
            segmented_image[i, j] = centroids[cluster_idx]

    # Convert the segmented image back to the BGR color space
    segmented_image = cv2.cvtColor(segmented_image, cv2.COLOR_HSV2BGR)

    # Return the original and segmented images
    return image, segmented_image
image_path = 'image.jpg'
n_clusters = 3
random_seed = 42