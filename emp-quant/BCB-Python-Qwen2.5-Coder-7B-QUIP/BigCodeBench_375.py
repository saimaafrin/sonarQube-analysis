
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(l):
    # Ensure the input is a numpy array
    l = np.array(l)
    
    # Perform PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(l)
    
    # Create a figure and axes
    ax = plt.subplots()[1]
    
    # Plot the first two principal components
    ax.scatter(principal_components[:, 0], principal_components[:, 1])
    ax.set_title('PCA Result')
    ax.set_xlabel('First Principal Component')
    ax.set_ylabel('Second Principal Component')
    
    # Return the axes object
    return ax