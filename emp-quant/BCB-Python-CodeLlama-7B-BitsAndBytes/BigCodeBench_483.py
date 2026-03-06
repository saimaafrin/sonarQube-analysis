
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
        The name of the column containing the words to be reversed.
    pattern : str
        The regular expression pattern to match the words.

    Returns
    -------
    pd.DataFrame
        A new pandas DataFrame with the specified column's words reordered, maintaining the original order of words that do not match, and returning a copy of the unaltered DataFrame if the pattern is empty.
    """
    def reverse_words(words: List[str]) -> List[str]:
        """
        Reverse the order of the words in a list.

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

    # Create a copy of the DataFrame to avoid modifying the original
    df_copy = df.copy()

    # Extract the column containing the words to be reversed
    words_column = df_copy[column_name]

    # Create a list of tuples containing the original index and the reversed words
    reversed_words = [(index, reverse_words(words)) for index, words in words_column.items()]

    # Create a new DataFrame with the reversed words
    reversed_df = pd.DataFrame(reversed_words, columns=['index', column_name])

    # If the pattern is empty, return a copy of the unaltered DataFrame
    if not pattern:
        return df_copy

    # Filter the DataFrame to only include rows where the words match the pattern
    filtered_df = reversed_df[reversed_df[column_name].str.match(pattern)]

    # Return the filtered DataFrame with the reversed words
    return filtered_df