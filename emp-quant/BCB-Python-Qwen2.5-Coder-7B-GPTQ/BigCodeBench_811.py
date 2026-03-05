import pandas as pd
from random import randint, seed
def task_func(dictionary, item, sample_size=None, random_seed=None):
    # Convert dictionary to DataFrame
    df = pd.DataFrame(dictionary)
    
    # Find positions of the item
    positions = [(row, col) for row in df.index for col in df.columns if df.at[row, col] == item]
    
    # Record frequency distribution
    frequency_distribution = df.apply(lambda x: (x == item).sum())
    
    # Optionally return a random sample of these positions
    if sample_size is not None:
        if random_seed is not None:
            seed(random_seed)
        sampled_positions = random.sample(positions, min(sample_size, len(positions)))
    else:
        sampled_positions = positions
    
    return sampled_positions, df, frequency_distribution
dictionary = {
    1: ['road', 'car', 'traffic'],
    2: ['car', 'light', 'candle']
}