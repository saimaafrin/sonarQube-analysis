
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def task_func(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Encrypt the categorical data in a specific column of a DataFrame using LabelEncoder.

    Parameters:
    df (pd.DataFrame): The DataFrame to be processed.
    column_name (str): The name of the column to be processed.

    Returns:
    pd.DataFrame: The DataFrame with the encoded column.
    """
    # Check if the column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column {column_name} does not exist in the DataFrame")

    # Get the unique values in the column
    unique_values = df[column_name].unique()

    # Create a LabelEncoder object
    le = LabelEncoder()

    # Fit the LabelEncoder object to the unique values in the column
    le.fit(unique_values)

    # Encode the column using the LabelEncoder object
    encoded_column = le.transform(df[column_name])

    # Create a new DataFrame with the encoded column
    encoded_df = pd.DataFrame(encoded_column, columns=[column_name])

    return encoded_df