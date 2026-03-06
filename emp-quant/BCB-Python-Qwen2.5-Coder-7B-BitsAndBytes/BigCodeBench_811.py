
import pandas as pd
from random import randint, seed

def task_func(dictionary, item, sample_size=None, random_seed=None):
    # Convert dictionary to DataFrame
    df = pd.DataFrame(dictionary).T
    
    # Find positions of the item
    positions = [(i, col) for i, row in enumerate(df.values) for col, value in enumerate(row) if value == item]
    
    # Record frequency distribution
    freq_distribution = df.apply(lambda x: (x == item).sum())
    
    # Randomly sample positions if sample_size is specified
    if sample_size is not None:
        if random_seed is not None:
            seed(random_seed)
        sampled_positions = [positions[randint(0, len(positions)-1)] for _ in range(sample_size)]
    else:
        sampled_positions = positions
    
    return sampled_positions, df, freq_distribution