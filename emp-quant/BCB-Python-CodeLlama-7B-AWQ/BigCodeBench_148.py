import pandas as pd
from sklearn.preprocessing import LabelEncoder
def task_func(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Encrypt the categorical data in a specific column of a DataFrame using LabelEncoder.
    """
    # Create a LabelEncoder object
    encoder = LabelEncoder()

    # Apply the LabelEncoder to the specified column
    df[column_name] = encoder.fit_transform(df[column_name])

    return df
df = pd.DataFrame({'A': ['a', 'b', 'c', 'a', 'b', 'c'],
                   'B': [1, 2, 3, 4, 5, 6],
                   'C': [7, 8, 9, 10, 11, 12]})