import re
import pandas as pd
def task_func(input_df):
    # Define a regular expression pattern to match special characters, punctuation, and spaces
    pattern = re.compile('[^a-zA-Z0-9]')
    
    # Apply the pattern to the 'text' column to remove unwanted characters
    input_df['clean_text'] = input_df['text'].apply(lambda x: pattern.sub('', x))
    
    # Calculate the length of the cleaned text and store it in a new column
    input_df['text_length'] = input_df['clean_text'].apply(len)
    
    # Return the DataFrame with the new columns
    return input_df