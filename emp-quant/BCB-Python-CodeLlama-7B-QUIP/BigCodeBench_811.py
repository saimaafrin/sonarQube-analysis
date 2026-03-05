
import pandas as pd
from random import randint, seed

def task_func(dictionary, item, sample_size=None, random_seed=None):
    df = pd.DataFrame(dictionary)
    positions = []
    for i, row in df.iterrows():
        for j, col in enumerate(row):
            if col == item:
                positions.append((i, j))
    if sample_size:
        sample = sample_size
        if random_seed:
            seed(random_seed)
        sample_positions = sample(positions, sample_size)
        return sample_positions
    return positions

dictionary = {
    1: ['road', 'car', 'traffic'],
    2: ['car', 'light', 'candle']
}

positions = task_func(dictionary, 'car')
print(positions)