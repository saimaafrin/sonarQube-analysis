
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("Input DataFrame is empty")
    
    # Perform PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(df)
    
    # Create a DataFrame with the principal components
    principal_components_df = pd.DataFrame(data=principal_components, columns=['Principal Component 1', 'Principal Component 2'])
    
    # Create a scatter plot of the principal components
    fig, ax = plt.subplots()
    ax.scatter(principal_components[:, 0], principal_components[:, 1], c='b', s=50)
    ax.set_title('2 Component PCA')
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    
    return principal_components_df, ax