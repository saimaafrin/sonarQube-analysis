import numpy as np
import pandas as pd
def task_func(df, letter):
    """
    This function converts an input dictionary into a DataFrame, filters rows where 'Word' column values start with a specified letter, calculates the lengths of these words, and returns basic statistics (mean, median, mode) of the word lengths.
    """
    # Convert the input dictionary to a DataFrame
    df = pd.DataFrame(df)

    # Filter the rows where 'Word' column values start with the specified letter
    df = df[df['Word'].str.startswith(letter)]

    # Calculate the lengths of the words
    df['Length'] = df['Word'].str.len()

    # Calculate the basic statistics of the word lengths
    stats = df['Length'].describe()

    # Return a dictionary of mean, median, and mode of word lengths
    return {'mean': stats['mean'], 'median': stats['50%'], 'mode': stats['mode']}
df = {'Word': ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']}
letter = 'e'