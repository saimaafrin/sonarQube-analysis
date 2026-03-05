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
    df['combination'] = df.apply(lambda row: tuple(row), axis=1)

    # Calculate the frequency of each combination
    counter = Counter(df['combination'])

    # Return a dictionary containing the frequency of all combination
    return dict(counter)
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8], 'C': [9, 10, 11, 12]})