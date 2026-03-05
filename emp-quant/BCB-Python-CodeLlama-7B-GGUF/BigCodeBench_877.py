
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def task_func(data, n_components=2):
    # Check if input data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a DataFrame")

    # Check if input data contains non-numeric data
    if not data.apply(lambda x: x.apply(lambda y: isinstance(y, (int, float)))).all().all():
        raise ValueError("Input data must contain only numeric data")

    # Check if n_components is greater than the number of columns in the data
    if n_components > data.shape[1]:
        raise ValueError("n_components must be less than or equal to the number of columns in the data")

    # Check if input data is empty
    if data.shape[0] == 0:
        raise ValueError("Input data must contain at least one row")

    # Scale the data using StandardScaler
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Apply PCA to reduce the number of dimensions of the data
    pca = PCA(n_components=n_components)
    pca_data = pca.fit_transform(scaled_data)

    # Create a new DataFrame with the original data transformed into 'n_components' principal components
    new_data = pd.DataFrame(pca_data, columns=["Principal Component 1", "Principal Component 2"])

    return new_data