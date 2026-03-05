
import pandas as pd
from random import randint, seed

def task_func(dictionary, item, sample_size=None, random_seed=None):
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(dictionary)
    
    # Find the positions of the item in the DataFrame
    positions = [(i, j) for i, row in enumerate(df.values) for j, value in enumerate(row) if value == item]
    
    # Record the frequency distribution of the item
    frequency = df.values.tolist().count(item)
    
    # Optionally return a random sample of these positions
    if sample_size is not None:
        if random_seed is not None:
            seed(random_seed)
        sample_positions = random.sample(positions, sample_size)
    else:
        sample_positions = positions
    
    return positions, df

positions, df = task_func(dictionary, 'car')
print("Positions:", positions)
print("DataFrame:")
print(df)