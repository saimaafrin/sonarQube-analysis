
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    # Perform PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(df)
    
    # Create a DataFrame with the principal components
    principal_df = pd.DataFrame(data=principal_components, columns=['Principal Component 1', 'Principal Component 2'])
    
    # Create a scatter plot of the two principal components
    fig, ax = plt.subplots()
    ax.scatter(principal_df['Principal Component 1'], principal_df['Principal Component 2'])
    
    # Set the title and labels
    ax.set_title('2 Component PCA')
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    
    return principal_df, ax