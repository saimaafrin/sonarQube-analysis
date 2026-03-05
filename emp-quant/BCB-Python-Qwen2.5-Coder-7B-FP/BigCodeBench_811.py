import pandas as pd
from random import randint, seed
def task_func(dictionary, item, sample_size=None, random_seed=None):
    # Convert dictionary to DataFrame
    df = pd.DataFrame(dictionary)
    
    # Find positions of the item
    positions = [(i, col) for i, row in df.iterrows() for col, value in row.items() if value == item]
    
    # Record frequency distribution
    frequency = df.apply(lambda x: (x == item).sum())
    
    # Optionally return a random sample of these positions
    if sample_size is not None:
        if random_seed is not None:
            seed(random_seed)
        sample_positions = random.sample(positions, sample_size)
    else:
        sample_positions = positions
    
    return sample_positions, df, frequency
dictionary = {1: ['road', 'car', 'traffic'], 2: ['car', 'light', 'candle']}