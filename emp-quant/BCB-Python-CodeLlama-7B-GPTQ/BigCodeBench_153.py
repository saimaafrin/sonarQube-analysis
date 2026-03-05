import pandas as pd
from sklearn.preprocessing import LabelEncoder
def task_func(data):
    # Create a LabelEncoder object
    encoder = LabelEncoder()

    # Encode the categorical data
    encoded_data = encoder.fit_transform(data)

    # Create a DataFrame with the original data and encoded data
    df = pd.DataFrame({'Category': data, 'Encoded': encoded_data})

    return df
data = ['A', 'B', 'C', 'A', 'B', 'C']