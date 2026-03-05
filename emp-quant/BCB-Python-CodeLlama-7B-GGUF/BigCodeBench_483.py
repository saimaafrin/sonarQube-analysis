
import re
import pandas as pd

def task_func(df: pd.DataFrame, column_name: str, pattern: str) -> pd.DataFrame:
    """
    Reverse the order of words in a specific column of a pandas DataFrame where the words match a user-specified regular expression pattern, using a nested helper function.
    Words are considered to be whitespace-separated strings. This function maintains the original order of non-matching words.

    Parameters
    ----------
    df : pd.DataFrame
        The pandas DataFrame to be processed.
    column_name : str
        The name of the column to be processed.
    pattern : str
        The regular expression pattern to match.

    Returns
    -------
    pd.DataFrame
        A new pandas DataFrame with the specified column's words reordered, maintaining the original order of words that do not match, and returning a copy of the unaltered DataFrame if the pattern is empty.
    """
    def reverse_words(words: List[str]) -> List[str]:
        """
        Reverse the order of a list of words.

        Parameters
        ----------
        words : List[str]
            The list of words to be reversed.

        Returns
        -------
        List[str]
            The reversed list of words.
        """
        return words[::-1]

    # Check if the pattern is empty
    if not pattern:
        return df.copy()

    # Extract the column of interest
    column = df[column_name]

    # Create a new column with the reversed words
    reversed_column = column.apply(lambda x: reverse_words(x.split()))

    # Create a new DataFrame with the reversed column
    new_df = df.copy()
    new_df[column_name] = reversed_column

    return new_df