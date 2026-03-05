import pandas as pd
import time
def task_func(df, letter):
    """
    The function filters rows in a dict of list in which the values of the 'Word' column begin with a specified letter. It first converts the dict to DataFrame, then calculates the length of the words in the filtered column and returns a dictionary of word lengths and their respective counts.
    """
    # Convert the dict to DataFrame
    df = pd.DataFrame(df)

    # Filter the rows based on the specified letter
    df = df[df['Word'].str.startswith(letter)]

    # Calculate the length of the words in the filtered column
    df['Word_length'] = df['Word'].str.len()

    # Group the DataFrame by the length of the words and count the number of occurrences
    df_grouped = df.groupby('Word_length')['Word'].count()

    # Convert the result to a dictionary
    result = df_grouped.to_dict()

    return result
df = {'Word': ['apple', 'banana', 'orange', 'grape', 'pear']}
letter = 'a'