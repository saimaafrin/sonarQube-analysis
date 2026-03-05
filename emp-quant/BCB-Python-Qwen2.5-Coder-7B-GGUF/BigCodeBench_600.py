
import numpy as np
import pandas as pd

def task_func(df, letter):
    # Filter rows where 'Word' column values start with the specified letter
    filtered_df = df[df['Word'].str.startswith(letter)]
    
    # Calculate the lengths of the words
    word_lengths = filtered_df['Word'].str.len()
    
    # Calculate basic statistics (mean, median, mode) of the word lengths
    stats = {
        'mean': np.mean(word_lengths),
        'median': np.median(word_lengths),
        'mode': word_lengths.mode()[0]
    }
    
    return stats