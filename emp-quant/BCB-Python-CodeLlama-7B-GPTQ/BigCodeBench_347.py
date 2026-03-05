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

    # Iterate over the column data
    for row in column_data:
        # Check if the row matches the pattern
        if re.search(PATTERN, row):
            # Add the match to the list of unique matches
            unique_matches.append(row)

    # Count the number of unique matches
    unique_counts = pd.Series(unique_matches).value_counts()

    # Return the Series with the unique counts
    return unique_counts
df = pd.DataFrame({"column1": ["a1b2c3d4", "a1b2c3d4", "a1b2c3d4", "a1b2c3d4", "a1b2c3d4"],
                   "column2": ["a1b2c3d4", "a1b2c3d4", "a1b2c3d4", "a1b2c3d4", "a1b2c3d4"]})