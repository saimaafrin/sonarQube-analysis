
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def task_func(data, n_components=2):
    # Check if input data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame.")
    
    # Check if input data is empty
    if data.empty:
        raise ValueError("Input data cannot be empty.")
    
    # Check if all columns in the data are numeric
    if not data.apply(pd.to_numeric, errors='coerce').notnull().all().all():
        raise ValueError("Input data must contain only numeric values.")
    
    # Check if n_components is greater than the number of columns in the data
    if n_components > data.shape[1]:
        raise ValueError("n_components cannot be greater than the number of columns in the data.")
    
    # Scale the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    
    # Apply PCA
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(scaled_data)
    
    # Create a new DataFrame with the principal components
    principal_df = pd.DataFrame(data=principal_components, columns=[f'PC{i+1}' for i in range(n_components)])
    
    return principal_df