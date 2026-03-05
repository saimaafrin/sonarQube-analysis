import re
import pandas as pd
def task_func(df: pd.DataFrame, column_name: str, pattern: str) -> pd.DataFrame:
    """
    Reverse the order of words in a specific column of a pandas DataFrame where the words match a user-specified regular expression pattern, using a nested helper function. Words are considered to be whitespace-separated strings. This function maintains the original order of non-matching words.
    The function should output with:
        pd.DataFrame: A new pandas DataFrame with the specified column's words reordered
        if they match the pattern, maintaining the original order of words that do not match,
        and returning a copy of the unaltered DataFrame if the pattern is empty.
    """
    # Create a copy of the input DataFrame
    df_copy = df.copy()

    # Define a nested helper function to reverse the order of words in a given string
    def reverse_words(string: str) -> str:
        """
        Reverse the order of words in a given string.
        """
        words = string.split()
        words.reverse()
        return " ".join(words)

    # Apply the nested helper function to the specified column of the copy of the input DataFrame
    df_copy[column_name] = df_copy[column_name].apply(reverse_words)

    # Return the modified copy of the input DataFrame
    return df_copy
df = pd.DataFrame({"A": ["This is a test sentence.", "This is another test sentence."], "B": [1, 2]})