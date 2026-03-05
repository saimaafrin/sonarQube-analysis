
import re
import pandas as pd

def task_func(df: pd.DataFrame, column_name: str, pattern: str) -> pd.DataFrame:
    """
    Reverses the order of words in a specific column of a pandas DataFrame where the words match a user-specified regular expression pattern.
    Words are considered to be whitespace-separated strings. This function maintains the original order of non-matching words.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column_name (str): The name of the column to process.
    pattern (str): The regular expression pattern to match words.
    
    Returns:
    pd.DataFrame: A new pandas DataFrame with the specified column's words reordered if they match the pattern, maintaining the original order of words that do not match, and returning a copy of the unaltered DataFrame if the pattern is empty.
    """
    
    # Helper function to reverse words in a string that match the pattern
    def reverse_words(text):
        words = text.split()
        reversed_words = []
        for word in words:
            if re.match(pattern, word):
                reversed_words.append(word[::-1])
            else:
                reversed_words.append(word)
        return ' '.join(reversed_words)
    
    # Check if the pattern is empty
    if not pattern:
        return df.copy()
    
    # Apply the helper function to the specified column
    df[column_name] = df[column_name].apply(reverse_words)
    
    return df