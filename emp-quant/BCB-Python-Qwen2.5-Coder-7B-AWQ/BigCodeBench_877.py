import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
def task_func(data, n_components=2):
    # Check if the input data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame.")
    
    # Check if the DataFrame is empty
    if data.empty:
        raise ValueError("Input data cannot be empty.")
    
    # Check if all columns in the DataFrame are numeric
    if not all(data.dtypes.apply(lambda x: np.issubdtype(x, np.number))):
        raise ValueError("All columns in the DataFrame must be numeric.")
    
    # Check if n_components is greater than the number of columns
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
data = pd.DataFrame({
    'A': [-43, 212, 1, -12, 5],
    'B': [-1, 0, 0, 9.76, 12.34],
    'C': [1, 42, -13.2, 31, 1.23],
})