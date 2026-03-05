
import re
import pandas as pd

def task_func(input_df):
    # Remove special characters, punctuation marks, and spaces
    input_df['clean_text'] = input_df['text'].str.replace(r'[^a-zA-Z0-9\s]', '')
    input_df['clean_text'] = input_df['clean_text'].str.replace(r'\s+', ' ')
    input_df['clean_text'] = input_df['clean_text'].str.strip()

    # Calculate the length of the cleaned text
    input_df['text_length'] = input_df['clean_text'].str.len()

    return input_df[['clean_text', 'text_length']]