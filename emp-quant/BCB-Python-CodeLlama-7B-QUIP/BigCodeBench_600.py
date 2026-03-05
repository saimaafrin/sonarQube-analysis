
import numpy as np
import pandas as pd

def task_func(df, letter):
    # Filter the rows where the 'Word' column values start with the specified letter
    df_filtered = df[df['Word'].str.startswith(letter)]

    # Calculate the lengths of the words in the filtered rows
    word_lengths = df_filtered['Word'].str.len()

    # Calculate the mean, median, and mode of the word lengths
    mean = np.mean(word_lengths)
    median = np.median(word_lengths)
    mode = np.mode(word_lengths)

    # Return a dictionary of the mean, median, and mode
    return {'mean': mean, 'median': median, 'mode': mode}