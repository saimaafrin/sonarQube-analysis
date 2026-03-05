import re
import pandas as pd
def task_func(input_df):
    """
    Cleans the text in a pandas DataFrame column named 'text' by removing all special characters, punctuation marks, and spaces, then calculates the length of the cleaned text.
    The function should output with:
        pandas.DataFrame: A DataFrame with two new columns 'clean_text' and 'text_length', where 'clean_text' is the cleaned text and 'text_length' is its length.
    """
    # Create a regular expression pattern to remove special characters, punctuation marks, and spaces
    pattern = re.compile(r'[^a-zA-Z0-9\s]')

    # Create a new column in the input DataFrame to store the cleaned text
    input_df['clean_text'] = input_df['text'].str.replace(pattern, '')

    # Calculate the length of the cleaned text
    input_df['text_length'] = input_df['clean_text'].str.len()

    # Return the cleaned DataFrame
    return input_df
input_df = pd.DataFrame({'text': ['Hello, world!', 'Hello, world!', 'Hello, world!']})