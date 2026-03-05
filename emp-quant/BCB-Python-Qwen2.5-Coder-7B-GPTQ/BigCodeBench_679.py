import pandas as pd
from collections import Counter
def task_func(df):
    # Generate combinations of elements in each row
    df['combination'] = df.apply(lambda row: tuple(sorted(row)), axis=1)
    
    # Calculate the frequency of each combination
    combination_counts = Counter(df['combination'])
    
    return combination_counts
df = pd.DataFrame({
    'item1': ['apple', 'banana', 'apple'],
    'item2': ['banana', 'apple', 'banana'],
    'item3': ['apple', 'banana', 'apple']
})