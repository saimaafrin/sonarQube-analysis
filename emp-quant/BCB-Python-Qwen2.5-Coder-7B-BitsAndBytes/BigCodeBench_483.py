
import re
import pandas as pd

def reverse_words_in_column(df: pd.DataFrame, column_name: str, pattern: str) -> pd.DataFrame:
    """
    Reverses the order of words in a specific column of a pandas DataFrame where the words match a user-specified 
    regular expression pattern, using a nested helper function. Words are considered to be whitespace-separated strings. 
    This function maintains the original order of non-matching words.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column_name (str): The name of the column to process.
    pattern (str): The regular expression pattern to match words for reversal.

    Returns:
    pd.DataFrame: A new pandas DataFrame with the specified column's words reordered if they match the pattern, 
                  maintaining the original order of words that do not match. Returns a copy of the unaltered DataFrame if the pattern is empty.
    """

    def reverse_word(word):
        """Helper function to reverse a word."""
        return ' '.join(reversed(word.split()))

    # Check if the pattern is empty
    if not pattern:
        return df.copy()

    # Apply the transformation only to the specified column
    df[column_name] = df[column_name].apply(lambda x: ' '.join(reverse_word(word) if re.search(pattern, word) else word for word in x.split()))
    
    return df