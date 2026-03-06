
import re
import pandas as pd

def task_func(input_df):
    # Define a regular expression pattern to match special characters, punctuation, and spaces
    pattern = r'[^\w\s]'
    
    # Apply the regex pattern to remove unwanted characters from the 'text' column
    input_df['clean_text'] = input_df['text'].str.replace(pattern, '', regex=True)
    
    # Remove any remaining whitespace from the 'clean_text' column
    input_df['clean_text'] = input_df['clean_text'].str.replace(r'\s+', '', regex=True)
    
    # Calculate the length of the cleaned text and store it in a new column 'text_length'
    input_df['text_length'] = input_df['clean_text'].str.len()
    
    return input_df