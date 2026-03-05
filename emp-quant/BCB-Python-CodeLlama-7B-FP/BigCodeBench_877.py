import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
def task_func(data, n_components=2):
    """
    Perform PCA (Principal Component Analysis) on the provided DataFrame.
    This function takes a pandas DataFrame, scales the data using sklearn StandardScaler,
    and then applies PCA to reduce the number of dimensions of the data to the number
    specified by n_components, maintaining as much information as possible.
    """
    # Check if input data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data is not a DataFrame")

    # Check if input data contains non-numeric data
    if not data.select_dtypes(include=[np.number]).empty:
        raise ValueError("Input data contains non-numeric data")

    # Check if n_components is greater than the number of columns in the data
    if n_components > data.shape[1]:
        raise ValueError("n_components is greater than the number of columns in the data")

    # Check if input data is empty
    if data.empty:
        raise ValueError("Input data is empty")

    # Scale the data using StandardScaler
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Apply PCA to reduce the number of dimensions of the data
    pca = PCA(n_components=n_components)
    pca_data = pca.fit_transform(scaled_data)

    # Create a new DataFrame with the original data transformed into 'n_components' principal components
    new_data = pd.DataFrame(pca_data, columns=data.columns)

    return new_data
data = pd.DataFrame({
    'A': [-43, 212, 1, -12, 5],
    'B': [-1, 0, 0, 9.76, 12.34],
    'C': [1, 42, -13.2, 31, 1.23],
})