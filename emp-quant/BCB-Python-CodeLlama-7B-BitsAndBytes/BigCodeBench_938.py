
import re
import pandas as pd

def task_func(input_df):
    # Create a new column in the DataFrame for the cleaned text
    input_df['clean_text'] = input_df['text'].str.replace(r'[^a-zA-Z0-9\s]', '')

    # Calculate the length of the cleaned text
    input_df['text_length'] = input_df['clean_text'].str.len()

    # Return the cleaned DataFrame
    return input_df