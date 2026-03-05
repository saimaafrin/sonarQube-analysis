import pandas as pd
import time
def task_func(df, letter):
    """
    This function filters rows in a dict of list in which the values of the 'Word' column begin with a specified letter. It first converts the dict to a DataFrame, then calculates the length of the words in the filtered column and returns a dictionary of word lengths and their respective counts.
    """
    # Convert the dict to a DataFrame
    df = pd.DataFrame(df)

    # Filter the rows in the DataFrame where the 'Word' column begins with the specified letter
    df = df[df['Word'].str.startswith(letter)]

    # Calculate the length of the words in the filtered column
    word_lengths = df['Word'].str.len()

    # Group the word lengths by their counts
    word_lengths_counts = word_lengths.value_counts()

    # Return a dictionary of word lengths and their counts
    return word_lengths_counts.to_dict()
df = {'Word': ['apple', 'banana', 'orange', 'mango', 'pineapple']}
letter = 'a'