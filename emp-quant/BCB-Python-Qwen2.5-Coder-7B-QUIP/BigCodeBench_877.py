
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def task_func(data, n_components=2):
    # Check if input data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame")
    
    # Check if input data is empty
    if data.empty:
        raise ValueError("Input data cannot be empty")
    
    # Check if n_components is greater than the number of columns in the data
    if n_components > data.shape[1]:
        raise ValueError("n_components cannot be greater than the number of columns in the data")
    
    # Scale the data using StandardScaler
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    
    # Apply PCA to reduce the number of dimensions
    pca = PCA(n_components=n_components)
    res = pca.fit_transform(scaled_data)
    
    # Convert the result to a DataFrame
    res_df = pd.DataFrame(res, columns=[f"PC{i}" for i in range(1, n_components + 1)])
    
    return res_df