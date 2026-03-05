
import pandas as pd
from collections import Counter

def task_func(df):
    # Generate combinations for each row
    df['combination'] = df.apply(lambda row: tuple(row), axis=1)
    
    # Calculate the frequency of each combination
    combination_counts = Counter(df['combination'])
    
    # Output the result as a dictionary
    return dict(combination_counts)