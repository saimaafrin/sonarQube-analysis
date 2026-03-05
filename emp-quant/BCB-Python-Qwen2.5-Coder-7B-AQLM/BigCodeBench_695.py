
import numpy as np
from sklearn.decomposition import PCA

def task_func(tuples_list, n_components):
    # Convert the list of tuples to a numpy array
    data = np.array(tuples_list)
    
    # Initialize the PCA model with the specified number of components
    pca = PCA(n_components=n_components)
    
    # Fit the PCA model to the data and transform it
    transformed_data = pca.fit_transform(data)
    
    return transformed_data