import numpy as np
import pandas as pd
def task_func(df, letter):
    # Filter rows where 'Word' column values start with the specified letter
    filtered_df = df[df['Word'].str.startswith(letter)]
    
    # Calculate the lengths of these words
    word_lengths = filtered_df['Word'].str.len()
    
    # Calculate basic statistics (mean, median, mode) of the word lengths
    stats = {
        'mean': word_lengths.mean(),
        'median': word_lengths.median(),
        'mode': word_lengths.mode()[0]
    }
    
    return stats