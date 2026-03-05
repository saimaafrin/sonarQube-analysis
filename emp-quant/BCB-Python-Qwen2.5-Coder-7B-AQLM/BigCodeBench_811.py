
import pandas as pd
from random import randint, seed

def task_func(dictionary, item, sample_size=None, random_seed=None):
    # Convert dictionary to DataFrame
    df = pd.DataFrame(dictionary)
    
    # Find positions of the item
    positions = [(row, col) for row in range(df.shape[0]) for col in range(df.shape[1]) if df.iloc[row, col] == item]
    
    # Record frequency distribution
    frequency_distribution = df[df == item].count().sum()
    
    # Optionally return a random sample of these positions
    if sample_size is not None:
        if random_seed is not None:
            seed(random_seed)
        sample_positions = [positions[randint(0, len(positions) - 1)] for _ in range(sample_size)]
        return sample_positions, df
    else:
        return positions, df