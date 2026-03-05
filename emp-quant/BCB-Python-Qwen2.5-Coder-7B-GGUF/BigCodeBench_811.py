
import pandas as pd
from random import randint, seed

def task_func(dictionary, item, sample_size=None, random_seed=None):
    # Convert dictionary to DataFrame
    df = pd.DataFrame(dictionary)
    
    # Find positions of the item
    positions = [(row, col) for row in range(df.shape[0]) for col in range(df.shape[1]) if df.iat[row, col] == item]
    
    # Record frequency distribution
    frequency_distribution = df.apply(lambda x: (x == item).sum()).to_frame()
    
    # Optionally return a random sample of these positions
    if sample_size is not None:
        if random_seed is not None:
            seed(random_seed)
        sample_positions = random.sample(positions, min(sample_size, len(positions)))
        return sample_positions, df, frequency_distribution
    else:
        return positions, df, frequency_distribution