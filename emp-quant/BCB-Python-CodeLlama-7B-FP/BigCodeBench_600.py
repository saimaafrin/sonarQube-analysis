import numpy as np
import pandas as pd
def task_func(df, letter):
    """
    This function converts an input dictionary into a DataFrame, filters rows where 'Word' column values start with a specified letter, calculates the lengths of these words, and returns basic statistics (mean, median, mode) of the word lengths.
    The function should output with:
        dict: A dictionary of mean, median, and mode of word lengths.
    """
    # Convert the input dictionary to a DataFrame
    df = pd.DataFrame(df)

    # Filter rows where 'Word' column values start with the specified letter
    df = df[df['Word'].str.startswith(letter)]

    # Calculate the lengths of the words
    lengths = df['Word'].str.len()

    # Calculate basic statistics of the word lengths
    mean = lengths.mean()
    median = lengths.median()
    mode = lengths.mode()

    # Return a dictionary of mean, median, and mode of word lengths
    return {'mean': mean, 'median': median, 'mode': mode}
df = {'Word': ['apple', 'banana', 'cherry', 'date', 'elderberry']}
letter = 'a'