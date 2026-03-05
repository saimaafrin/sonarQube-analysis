
import pandas as pd
from collections import Counter

def task_func(df):
    # Add a 'combination' column to the DataFrame
    df['combination'] = df[['A', 'B', 'C']].apply(lambda x: ''.join(x), axis=1)

    # Calculate the frequency of each combination
    combination_counts = Counter(df['combination'])

    # Return a dictionary containing the frequency of all combinations
    return dict(combination_counts)