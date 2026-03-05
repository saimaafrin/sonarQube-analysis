import re
import pandas as pd
def task_func(df: pd.DataFrame, column_name: str, pattern: str) -> pd.DataFrame:
    """
    Reverses the order of words in a specific column of a pandas DataFrame where the words match a user-specified regular expression pattern.
    Words are considered to be whitespace-separated strings. This function maintains the original order of non-matching words.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - column_name (str): The name of the column to process.
    - pattern (str): The regular expression pattern to match words.
    
    Returns:
    - pd.DataFrame: A new pandas DataFrame with the specified column's words reordered if they match the pattern, maintaining the original order of words that do not match, and returning a copy of the unaltered DataFrame if the pattern is empty.
    """
    if not pattern:
        return df.copy()
    
    def reverse_words_in_match(match):
        words = match.group().split()
        return ' '.join(reversed(words))
    
    df_copy = df.copy()
    df_copy[column_name] = df_copy[column_name].str.replace(pattern, reverse_words_in_match, regex=True)
    return df_copy
df = pd.DataFrame({'text': ['hello world', 'foo bar', 'baz qux', 'hello world again']})