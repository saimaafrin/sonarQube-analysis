
import pandas as pd
from collections import Counter

def task_func(df):
    # Add a 'combination' column to the DataFrame
    df['combination'] = df.apply(lambda row: ''.join(row.values()), axis=1)

    # Calculate the frequency of each combination
    counter = Counter(df['combination'])

    # Return a dictionary containing the frequency of all combinations
    return dict(counter)