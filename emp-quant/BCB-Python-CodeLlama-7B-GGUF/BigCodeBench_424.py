
import cv2
import numpy as np
import os
from sklearn.cluster import KMeans

def task_func(image_path='image.jpg', n_clusters=3, random_seed=42):
    # Check if image file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file {image_path} does not exist")

    # Load image
    image = cv2.imread(image_path)

    # Check if n_clusters is a positive integer
    if not isinstance(n_clusters, int) or n_clusters <= 0:
        raise ValueError(f"n_clusters must be a positive integer, got {n_clusters}")

    # Convert image to RGB
    if image.ndim == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    elif image.ndim == 3 and image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:
        raise ValueError(f"Image must be RGB, got {image.shape[2]} channels")

    # Apply K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_seed)
    labels = kmeans.fit_predict(image.reshape(-1, 3))
    centroids = kmeans.cluster_centers_

    # Create segmented image
    segmented_image = np.zeros_like(image)
    for i in range(n_clusters):
        segmented_image[labels == i] = centroids[i]

    # Return original and segmented images
    return image, segmented_image