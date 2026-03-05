
import pandas as pd
import re
import numpy as np

# Constants
PATTERN = r"([a-fA-F\d]{32})"

def task_func(df, column):
    # Check if the column exists in the DataFrame
    if column not in df.columns:
        raise KeyError(f"The column '{column}' does not exist in the input DataFrame.")
    
    # Find all matches of the regex pattern in the specified column
    matches = df[column].str.findall(PATTERN).explode()
    
    # Count the occurrence of each unique match
    match_counts = matches.value_counts()
    
    return match_counts