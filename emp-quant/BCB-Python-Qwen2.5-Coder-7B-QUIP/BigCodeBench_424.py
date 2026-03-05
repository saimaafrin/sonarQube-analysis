
import cv2
import numpy as np
import os
from sklearn.cluster import KMeans
from PIL import Image

def task_func(image_path='image.jpg', n_clusters=3, random_seed=42):
    # Check if the image file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found at {image_path}")

    # Check if n_clusters is a positive integer
    if not isinstance(n_clusters, int) or n_clusters <= 0:
        raise ValueError("n_clusters must be a positive integer")

    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Failed to load image")

    # Reshape the image to a 2D array of pixels
    pixels = image.reshape(-1, 3)

    # Perform K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_seed)
    labels = kmeans.fit_predict(pixels)
    centroids = kmeans.cluster_centers_

    # Replace each pixel with the centroid color
    segmented_image = np.zeros_like(pixels)
    for i, centroid in enumerate(centroids):
        mask = labels == i
        segmented_image[mask] = centroid

    # Reshape the segmented image back to the original image shape
    segmented_image = segmented_image.reshape(image.shape)

    # Save the segmented image
    _, filename = os.path.split(image_path)
    segmented_filename = f"segmented_{filename}"
    cv2.imwrite(segmented_filename, segmented_image)

    # Return the original and segmented images as numpy arrays
    return image, segmented_image