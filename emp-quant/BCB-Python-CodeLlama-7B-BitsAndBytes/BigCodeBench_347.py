
import pandas as pd
import re
import numpy as np

# Constants
PATTERN = r"([a-fA-F\d]{32})"

def task_func(df, column):
    """
    Find all matches of the regex pattern '([a-fA-F\ d] {32})' in a Pandas DataFrame column and count the occurrence of any unique match in the data.

    Args:
        df (pd.DataFrame): Input DataFrame.
        column (str): Name of the column to search in.

    Returns:
        pd.Series: A pandas Series with counts of each unique match.

    Raises:
        KeyError: If the "column" does not exist in input "df".
    """
    if column not in df.columns:
        raise KeyError(f"Column {column} does not exist in input DataFrame.")

    # Create a new column to store the matches
    df["matches"] = df[column].str.extract(PATTERN)

    # Count the unique matches
    unique_matches = df["matches"].value_counts()

    # Drop the temporary column
    df.drop(columns=["matches"], inplace=True)

    return unique_matches