import pandas as pd
from sklearn.preprocessing import LabelEncoder
def task_func(data):
    """
    Transforms categorical data into a numerical format suitable for machine learning algorithms using sklearn's LabelEncoder.
    This function generates a DataFrame that pairs original categorical values with their numerical encodings.
    The function should output with:
        DataFrame: A DataFrame with columns 'Category' and 'Encoded', where 'Category' is the original data and 'Encoded'
        is the numerical representation.
    """
    # Create a LabelEncoder object
    encoder = LabelEncoder()

    # Encode the categorical data
    encoded_data = encoder.fit_transform(data)

    # Create a DataFrame with the encoded data
    encoded_df = pd.DataFrame({'Category': data, 'Encoded': encoded_data})

    return encoded_df
data = ['A', 'B', 'C', 'A', 'B', 'C']