
import pandas as pd
import re
import numpy as np

# Constants
PATTERN = r"([a-fA-F\d]{32})"

def task_func(df, column):
    """
    Find all matches of the regex pattern '([a-fA-F\d]{32})' in a Pandas DataFrame column 
    and count the occurrence of any unique match in the data.

    Parameters:
    df (pd.DataFrame): Input DataFrame.
    column (str): Name of the column to search for matches.

    Returns:
    pd.Series: A pandas Series with counts of each unique match.

    Raises:
    KeyError: If the specified column does not exist in the DataFrame.
    """

    # Check if the column exists in the DataFrame
    if column not in df.columns:
        raise KeyError(f"The column '{column}' does not exist in the DataFrame.")

    # Extract matches using regex
    matches = df[column].str.extractall(PATTERN).reset_index(drop=True)

    # Count occurrences of each unique match
    result = matches.value_counts()

    return result