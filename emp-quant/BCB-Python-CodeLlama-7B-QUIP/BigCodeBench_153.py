
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def task_func(data):
    # Create a LabelEncoder object
    le = LabelEncoder()

    # Fit the LabelEncoder to the data
    le.fit(data)

    # Transform the data using the LabelEncoder
    encoded_data = le.transform(data)

    # Create a DataFrame with the original data and the encoded data
    df = pd.DataFrame({'Category': data, 'Encoded': encoded_data})

    return df