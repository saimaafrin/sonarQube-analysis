import pandas as pd
from sklearn.preprocessing import LabelEncoder
def task_func(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Encrypt the categorical data in a specific column of a DataFrame using LabelEncoder.
    """
    # Create a LabelEncoder object
    encoder = LabelEncoder()

    # Encode the categorical data in the specified column
    encoded_column = encoder.fit_transform(df[column_name])

    # Create a new DataFrame with the encoded column
    encoded_df = pd.DataFrame(encoded_column, columns=[column_name])

    return encoded_df
df = pd.DataFrame({'A': ['a', 'b', 'c', 'a', 'b', 'c'],
                   'B': [1, 2, 3, 4, 5, 6],
                   'C': [7, 8, 9, 10, 11, 12]})