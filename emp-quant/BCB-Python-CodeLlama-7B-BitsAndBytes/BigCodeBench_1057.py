
import pandas as pd
import itertools
import numpy as np

def task_func(animals=None, foods=None):
    # Handle special cases
    if animals is None or foods is None:
        return pd.DataFrame()
    if len(animals) == 0 or len(foods) == 0:
        animals = ['cat', 'dog', 'bird']
        foods = ['apple', 'banana', 'orange']

    # Generate all possible combinations of animals and foods
    animal_food_pairs = list(itertools.product(animals, foods))

    # Shuffle the pairs randomly
    np.random.shuffle(animal_food_pairs)

    # Create a DataFrame with the pairs
    df = pd.DataFrame(animal_food_pairs, columns=['animal', 'food'])

    return df