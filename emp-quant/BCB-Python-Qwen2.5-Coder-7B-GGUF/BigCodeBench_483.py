
import re
import pandas as pd

def task_func(df: pd.DataFrame, column_name: str, pattern: str) -> pd.DataFrame:
    """
    Reverses the order of words in a specific column of a pandas DataFrame where the words match a user-specified regular expression pattern.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - column_name (str): The name of the column to process.
    - pattern (str): The regular expression pattern to match words.
    
    Returns:
    - pd.DataFrame: A new DataFrame with the specified column's words reordered if they match the pattern, maintaining the original order of words that do not match.
    """
    
    # Helper function to reverse words matching the pattern
    def reverse_matching_words(words):
        return [word[::-1] if re.match(pattern, word) else word for word in words]
    
    # Apply the helper function to the specified column
    df[column_name] = df[column_name].apply(lambda x: ' '.join(reverse_matching_words(x.split())))
    
    return df