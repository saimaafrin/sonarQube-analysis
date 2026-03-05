
import cv2
import numpy as np
import os
from sklearn.cluster import KMeans

def task_func(image_path='image.jpg', n_clusters=3, random_seed=42):
    # Load the image
    image = cv2.imread(image_path)

    # Convert to RGB
    image = image[:, :, ::3]

    # Apply K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_seed)
    kmeans.fit(image.reshape(-1, 3))
    centroids = kmeans.cluster_centers_

    # Replace pixel colors with centroid colors
    segmented_image = np.copy(image)
    for i in range(n_clusters):
        segmented_image[np.where(image == centroids[i])] = centroids[i]

    # Return the original and segmented images
    return (image, segmented_image)