
import pandas as pd
from collections import Counter

def task_func(df):
    # Create a new column 'combination' with the combination of items in each row
    df['combination'] = df[['A', 'B', 'C']].agg('-'.join, axis=1)

    # Calculate the frequency of each combination
    counter = Counter(df['combination'])

    # Convert the counter to a dictionary
    freq_dict = dict(counter)

    return freq_dict