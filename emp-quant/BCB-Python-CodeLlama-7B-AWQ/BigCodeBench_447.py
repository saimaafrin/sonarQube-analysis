import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
def task_func(data, n_components=2, random_state=None):
    # Perform PCA on the data
    pca = PCA(n_components=n_components, random_state=random_state)
    transformed_data = pca.fit_transform(data)

    # Create a scatter plot of the transformed data
    fig, ax = plt.subplots()
    ax.scatter(transformed_data[:, 0], transformed_data[:, 1], c=data[:, 2])

    # Return the transformed data and the scatter plot
    return {"transformed_data": transformed_data, "ax": ax}
data = np.random.rand(100, 3)