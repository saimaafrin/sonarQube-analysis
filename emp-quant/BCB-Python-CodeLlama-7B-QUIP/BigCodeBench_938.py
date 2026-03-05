
import re
import pandas as pd

def task_func(input_df):
    # Clean the text in the 'text' column
    input_df['clean_text'] = input_df['text'].str.replace(r'[^a-zA-Z0-9]', '')

    # Calculate the length of the cleaned text
    input_df['text_length'] = input_df['clean_text'].str.len()

    # Return the DataFrame with the new columns
    return input_df[['clean_text', 'text_length']]