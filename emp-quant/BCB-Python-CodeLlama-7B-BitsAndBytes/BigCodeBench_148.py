
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def task_func(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Encrypt the categorical data in a specific column of a DataFrame using LabelEncoder.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the categorical data.
    column_name (str): The name of the column containing the categorical data.

    Returns:
    pd.DataFrame: The DataFrame with the encoded column.
    """
    # Create a new column in the DataFrame to store the encoded data
    encoded_column = df[column_name].apply(LabelEncoder().fit_transform)

    # Create a new DataFrame with the encoded column
    encoded_df = pd.DataFrame(encoded_column, columns=[column_name])

    return encoded_df