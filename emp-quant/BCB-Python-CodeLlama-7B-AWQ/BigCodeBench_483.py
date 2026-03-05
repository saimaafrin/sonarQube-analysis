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
    def reverse_words(words: list[str]) -> list[str]:
        """
        Reverse the order of words in a list of whitespace-separated strings.
        """
        return words[::-1]

    # Create a copy of the input DataFrame
    df_copy = df.copy()

    # Get the column of interest
    column = df_copy[column_name]

    # Create a list of words in the column
    words = column.str.split()

    # Create a list of words that match the pattern
    matching_words = [word for word in words if re.match(pattern, word)]

    # Reverse the order of the matching words
    matching_words = reverse_words(matching_words)

    # Replace the matching words in the column
    column = column.str.replace(words, matching_words)

    # Replace the column in the DataFrame
    df_copy[column_name] = column

    return df_copy
df = pd.DataFrame({'A': ['apple', 'banana', 'orange', 'grape', 'pear'],
                   'B': ['cat', 'dog', 'fish', 'bird', 'rat']})