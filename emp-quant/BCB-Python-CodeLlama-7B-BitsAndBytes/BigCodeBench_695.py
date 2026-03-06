
import numpy as np
from sklearn.decomposition import PCA

def task_func(tuples_list, n_components):
    # Convert the list of tuples to a numpy array
    data = np.array(tuples_list)

    # Perform PCA on the data
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data)

    # Return the transformed data
    return transformed_data