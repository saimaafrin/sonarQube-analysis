
import pandas as pd
import re
import numpy as np
# Constants
PATTERN = r"([a-fA-F\d]{32})"
def task_func(df, column):
    # Check if the column exists in the dataframe
    if column not in df:
        raise KeyError("Column does not exist in the dataframe")
    # Extract the matches from the column
    matches = df[column].str.extract(PATTERN)
    # Count the unique matches
    unique_matches = matches.unique()
    # Create a pandas Series with the counts
    counts = pd.Series(unique_matches.count(), index=unique_matches)
    return counts