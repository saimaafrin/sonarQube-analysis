
import pandas as pd
from collections import Counter

def task_func(df):
    # Generate combinations for each row and store them in a new column
    df['combination'] = df.apply(lambda row: tuple(sorted(row)), axis=1)
    
    # Calculate the frequency of each combination
    combination_counts = df['combination'].value_counts().to_dict()
    
    return combination_counts