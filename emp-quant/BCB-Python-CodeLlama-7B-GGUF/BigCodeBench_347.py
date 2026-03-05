
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

    # Extract the column from the DataFrame
    column_data = df[column]

    # Create a list to store the unique matches
    unique_matches = []

    # Iterate over the column data and find all matches
    for row in column_data:
        match = re.search(PATTERN, row)
        if match:
            unique_matches.append(match.group(1))

    # Create a Series with the counts of each unique match
    match_counts = pd.Series(unique_matches).value_counts()

    return match_counts