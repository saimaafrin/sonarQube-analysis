import pandas as pd
import re
import numpy as np
PATTERN = r"([a-fA-F\d]{32})"
def task_func(df, column):
    """
    Find all matches of the regex pattern '([a-fA-F\d]{32})' in a Pandas DataFrame column and count the occurrence of any unique match in the data.
    
    Args:
    df (pd.DataFrame): The input DataFrame.
    column (str): The name of the column to search for matches.
    
    Returns:
    pd.Series: A pandas Series with counts of each unique match.
    
    Raises:
    KeyError: If the "column" does not exist in input "df".
    """
    # Check if the column exists in the DataFrame
    if column not in df.columns:
        raise KeyError(f"Column '{column}' does not exist in the DataFrame.")
    
    # Find all matches of the regex pattern in the specified column
    matches = df[column].str.findall(PATTERN)
    
    # Flatten the list of lists into a single list of matches
    all_matches = [match for sublist in matches for match in sublist]
    
    # Count the occurrence of each unique match
    match_counts = pd.Series(all_matches).value_counts()
    
    return match_counts