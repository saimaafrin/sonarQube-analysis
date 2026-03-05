
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def task_func(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    # Create a LabelEncoder object
    le = LabelEncoder()

    # Get the column with the specified name
    column = df[column_name]

    # Encode the column using the LabelEncoder
    encoded_column = le.fit_transform(column)

    # Create a new DataFrame with the encoded column
    new_df = pd.DataFrame(encoded_column, columns=[column_name])

    return new_df