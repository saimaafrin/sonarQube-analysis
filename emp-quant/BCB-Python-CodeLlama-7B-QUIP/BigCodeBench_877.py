
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def task_func(data, n_components=2):
    # Check if input data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a DataFrame")

    # Check if input data contains non-numeric data
    if not data.select_dtypes(include=[np.number]).empty:
        raise ValueError("Input data cannot contain non-numeric data")

    # Check if n_components is greater than the number of columns in the data
    if n_components > data.shape[1]:
        raise ValueError("n_components cannot be greater than the number of columns in the data")

    # Check if input data is empty
    if data.empty:
        raise ValueError("Input data cannot be empty")

    # Scale the data using StandardScaler
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Apply PCA to reduce the number of dimensions of the data
    pca = PCA(n_components=n_components)
    pca_data = pca.fit_transform(scaled_data)

    # Create a new DataFrame with the original data transformed into 'n_components' principal components
    new_data = pd.DataFrame(pca_data, columns=['PC' + str(i) for i in range(1, n_components + 1)])

    return new_data