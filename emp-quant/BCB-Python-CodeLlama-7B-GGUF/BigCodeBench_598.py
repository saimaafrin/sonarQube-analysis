
import pandas as pd
import time

def task_func(df, letter):
    """
    Function that filters rows in a dict of list in which the values of the 'Word' column begin with a specified letter.
    It first converts the dict to a DataFrame, then calculates the length of the words in the filtered column and returns a dictionary of word lengths and their respective counts.
    """
    # Convert dict to DataFrame
    df = pd.DataFrame(df)

    # Filter rows where the 'Word' column begins with the specified letter
    df = df[df['Word'].str.startswith(letter)]

    # Calculate the length of the words in the filtered column
    df['Word_Length'] = df['Word'].str.len()

    # Group the DataFrame by the 'Word_Length' column and calculate the count of each length
    df_grouped = df.groupby('Word_Length')['Word_Length'].count()

    # Convert the grouped DataFrame to a dictionary
    word_lengths_dict = df_grouped.to_dict()

    return word_lengths_dict

# Call the function and print the output
print(task_func(df, letter))