import pandas as pd
import time
def task_func(df, letter):
    # Filter rows where the 'Word' column values start with the specified letter
    filtered_df = df[df['Word'].str.startswith(letter)]
    
    # Calculate the length of each word in the filtered column
    word_lengths = filtered_df['Word'].apply(len)
    
    # Create a dictionary of word lengths and their counts
    length_counts = word_lengths.value_counts().to_dict()
    
    return length_counts