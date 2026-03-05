import pandas as pd
import re
import numpy as np
PATTERN = r"([a-fA-F\d]{32})"
def task_func(df, column):
    """
    Find all matches of the regex pattern '([a-fA-F\ d] {32})' in a Pandas DataFrame column and count the occurrence of any unique match in the data.
    The function should raise the exception for:
        - The function will raise KeyError if the "column" does not exist in input "df"
    The function should output with:
        - Series: A pandas Series with counts of each unique match.
    """
    # Check if the column exists in the DataFrame
    if column not in df.columns:
        raise KeyError(f"Column {column} does not exist in the DataFrame")

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
    unique_match_counts = pd.Series(unique_matches).value_counts()

    return unique_match_counts
df = pd.DataFrame({"column1": ["a1b2c3d4", "e5f6g7h8", "i9j0k1l2", "a1b2c3d4", "e5f6g7h8"]})