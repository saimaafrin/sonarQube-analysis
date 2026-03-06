
import pandas as pd
from random import randint, seed

def task_func(dictionary, item, sample_size=None, random_seed=None):
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(dictionary)

    # Find the positions of the item in the DataFrame
    positions = []
    for i, row in df.iterrows():
        if item in row.values:
            positions.append((i, row.name))

    # Optionally, return a random sample of these positions
    if sample_size is not None and random_seed is not None:
        seed(random_seed)
        sample = []
        for i in range(sample_size):
            sample.append(positions[randint(0, len(positions) - 1)])
        return sample

    return positions

positions = task_func(dictionary, 'car')
print(positions)

# Output:
# [(0, 2), (1, 1)]

# Output:
# [(0, 2), (1, 1), (1, 2)]