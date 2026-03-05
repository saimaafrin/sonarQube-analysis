import re
import pandas as pd
def task_func(input_df):
    """
    Cleans the text in a pandas DataFrame column named 'text' by removing all special characters, punctuation marks, and spaces, then calculates the length of the cleaned text.
    The function should output with:
        pandas.DataFrame: A DataFrame with two new columns 'clean_text' and 'text_length', where 'clean_text' is the cleaned text and 'text_length' is its length.
    """
    # Remove special characters, punctuation marks, and spaces
    input_df['clean_text'] = input_df['text'].str.replace(r'[^a-zA-Z0-9\s]', '')
    # Calculate the length of the cleaned text
    input_df['text_length'] = input_df['clean_text'].str.len()
    return input_df[['clean_text', 'text_length']]
input_df = pd.DataFrame({'text': ['Hello, world!', 'How are you?', 'I am fine, thank you.']})