
import numpy as np
import pandas as pd

def task_func(df, letter):
    # Convert the input dictionary to a DataFrame
    df = pd.DataFrame(df)

    # Filter rows where 'Word' column values start with the specified letter
    df = df[df['Word'].str.startswith(letter)]

    # Calculate the lengths of the words
    lengths = df['Word'].str.len()

    # Calculate the mean, median, and mode of the word lengths
    mean = lengths.mean()
    median = lengths.median()
    mode = lengths.mode()[0]

    # Create a dictionary of the mean, median, and mode of word lengths
    dict = {'mean': mean, 'median': median, 'mode': mode}

    return dict