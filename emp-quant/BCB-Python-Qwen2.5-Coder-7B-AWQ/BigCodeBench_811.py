import pandas as pd
from random import randint, seed
def task_func(dictionary, item, sample_size=None, random_seed=None):
    # Convert dictionary to pandas DataFrame
    df = pd.DataFrame(dictionary)
    
    # Find positions of the item in the DataFrame
    positions = [(i, j) for i, row in enumerate(df.values) for j, value in enumerate(row) if value == item]
    
    # Record frequency distribution of positions
    position_counts = pd.Series(positions).value_counts()
    
    # Optionally return a random sample of these positions
    if sample_size is not None:
        if random_seed is not None:
            seed(random_seed)
        sampled_positions = position_counts.sample(n=sample_size, replace=False).index.tolist()
    else:
        sampled_positions = None
    
    return positions, df, sampled_positions
dictionary = {1: ['road', 'car', 'traffic'], 2: ['car', 'light', 'candle']}