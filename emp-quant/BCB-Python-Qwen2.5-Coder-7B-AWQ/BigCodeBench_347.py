import pandas as pd
import re
import numpy as np
PATTERN = r"([a-fA-F\d]{32})"
def task_func(df, column):
    """
    Find all matches of the regex pattern '([a-fA-F\d]{32})' in a Pandas DataFrame column and count the occurrence of any unique match in the data.
    
    Args:
    df (pd.DataFrame): The input DataFrame.
    column (str): The name of the column to search for the pattern.
    
    Returns:
    pd.Series: A pandas Series with counts of each unique match.
    
    Raises:
    KeyError: If the "column" does not exist in input "df".
    """
    # Check if the column exists in the DataFrame
    if column not in df.columns:
        raise KeyError(f"The column '{column}' does not exist in the DataFrame.")
    
    # Find all matches of the regex pattern
    matches = df[column].str.findall(PATTERN).explode()
    
    # Count the occurrence of each unique match
    match_counts = matches.value_counts()
    
    return match_counts