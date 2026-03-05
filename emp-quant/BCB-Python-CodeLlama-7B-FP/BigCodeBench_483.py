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
    def reverse_words(words: List[str]) -> List[str]:
        """
        Reverse the order of words in a list of whitespace-separated strings.
        """
        return words[::-1]

    # Create a copy of the input DataFrame to avoid modifying the original
    df_copy = df.copy()

    # Get the column of interest
    column = df_copy[column_name]

    # Apply the regular expression pattern to the column
    matches = re.findall(pattern, column)

    # Reverse the order of the words in the matches
    reversed_matches = [reverse_words(match) for match in matches]

    # Replace the original column with the reversed matches
    df_copy[column_name] = reversed_matches

    return df_copy
df = pd.DataFrame({"A": ["hello world", "goodbye world", "hello universe", "goodbye universe"]})