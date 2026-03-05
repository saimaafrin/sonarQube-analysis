
import pandas as pd
import itertools
import numpy as np

def task_func(animals=None, foods=None):
    # Handle special cases
    if animals is None or len(animals) == 0:
        animals = ['cat', 'dog', 'bird']
    if foods is None or len(foods) == 0:
        foods = ['apple', 'banana', 'orange']

    # Generate all possible combinations of animals and foods
    combinations = itertools.product(animals, foods)

    # Shuffle the combinations randomly
    np.random.shuffle(combinations)

    # Create a DataFrame with the combinations
    df = pd.DataFrame(combinations, columns=['animal', 'food'])

    # Format the DataFrame
    df['animal:food'] = df['animal'] + ': ' + df['food']
    df = df.drop(columns=['animal', 'food'])

    return df