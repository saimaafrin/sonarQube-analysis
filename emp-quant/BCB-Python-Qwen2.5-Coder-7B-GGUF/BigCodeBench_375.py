
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(l):
    # Convert the input list to a numpy array
    data = np.array(l)
    
    # Initialize the PCA model with 2 components
    pca = PCA(n_components=2)
    
    # Fit the PCA model to the data
    pca.fit(data)
    
    # Transform the data to the new PCA space
    transformed_data = pca.transform(data)
    
    # Create a new figure
    fig, ax = plt.subplots()
    
    # Plot the transformed data
    ax.scatter(transformed_data[:, 0], transformed_data[:, 1])
    
    # Set the title and labels
    ax.set_title('PCA Result')
    ax.set_xlabel('First Principal Component')
    ax.set_ylabel('Second Principal Component')
    
    # Return the Axes object
    return ax