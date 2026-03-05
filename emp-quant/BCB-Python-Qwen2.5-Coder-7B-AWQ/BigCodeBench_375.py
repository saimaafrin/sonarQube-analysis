from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
def task_func(l):
    """
    Perform Principal Component Analysis (PCA) on the given array and record the first two main components.
    
    Parameters:
    l (list of lists): The input array to perform PCA on.
    
    Returns:
    ax (matplotlib.axes._axes.Axes): Axes object of the generated plot
    """
    # Convert the list of lists to a numpy array
    data = np.array(l)
    
    # Initialize PCA with 2 components
    pca = PCA(n_components=2)
    
    # Fit the PCA model to the data
    pca.fit(data)
    
    # Transform the data to the principal component space
    transformed_data = pca.transform(data)
    
    # Create a new figure and axis
    fig, ax = plt.subplots()
    
    # Plot the transformed data
    ax.scatter(transformed_data[:, 0], transformed_data[:, 1])
    
    # Set the title and labels
    ax.set_title('PCA Result')
    ax.set_xlabel('First Principal Component')
    ax.set_ylabel('Second Principal Component')
    
    # Return the axis object
    return ax