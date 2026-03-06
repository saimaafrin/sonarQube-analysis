
import numpy as np
import pandas as pd

def task_func(df, letter):
    # Filter rows where 'Word' column values start with the specified letter
    filtered_df = df[df['Word'].str.startswith(letter)]
    
    # Calculate the lengths of the words in the filtered DataFrame
    word_lengths = filtered_df['Word'].apply(len)
    
    # Calculate basic statistics (mean, median, mode) of the word lengths
    stats = {
        'Mean': word_lengths.mean(),
        'Median': word_lengths.median(),
        'Mode': word_lengths.mode()[0]
    }
    
    return stats