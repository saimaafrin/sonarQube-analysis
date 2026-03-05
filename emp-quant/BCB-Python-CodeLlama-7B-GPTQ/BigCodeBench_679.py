import pandas as pd
from collections import Counter
def task_func(df):
    """
    Calculate the frequency of combinations of elements in a DataFrame.
    The function adds a 'combination' column to the DataFrame, which is the combination of items in each row.
    It then calculates the frequency of each combination.
    The function should output with:
        dict: A dictionary containing the frequency of all combination.
    """
    # Add a 'combination' column to the DataFrame
    df['combination'] = df.apply(lambda row: tuple(row[['col1', 'col2']]), axis=1)

    # Calculate the frequency of each combination
    counter = Counter(df['combination'])

    # Convert the counter to a dictionary
    freq_dict = dict(counter)

    return freq_dict
df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [6, 7, 8, 9, 10]})