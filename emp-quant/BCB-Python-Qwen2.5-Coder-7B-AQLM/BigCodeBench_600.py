
import numpy as np
import pandas as pd

def task_func(df, letter):
    # Filter rows where 'Word' column values start with the specified letter
    filtered_df = df[df['Word'].str.startswith(letter)]
    
    # Calculate the lengths of the words
    word_lengths = filtered_df['Word'].str.len()
    
    # Calculate basic statistics (mean, median, mode) of the word lengths
    mean_length = np.mean(word_lengths)
    median_length = np.median(word_lengths)
    mode_length = np.mode(word_lengths)[0][0]
    
    # Return the results in a dictionary
    return {
        'mean': mean_length,
        'median': median_length,
        'mode': mode_length
    }