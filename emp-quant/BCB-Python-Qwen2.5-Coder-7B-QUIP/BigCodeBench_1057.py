
import pandas as pd
import itertools
import numpy as np

def task_func(animals=None, foods=None):
    # Default lists if none provided
    default_animals = ['Lion', 'Tiger', 'Bear', 'Elephant']
    default_foods = ['Meat', 'Fish', 'Grass', 'Fruit']

    # Use default lists if none provided
    if animals is None:
        animals = default_animals
    if foods is None:
        foods = default_foods

    # Check if both lists are empty
    if not animals or not foods:
        return pd.DataFrame()

    # Generate all combinations and shuffle them
    combinations = list(itertools.product(animals, foods))
    np.random.shuffle(combinations)

    # Create DataFrame
    df = pd.DataFrame(combinations, columns=['animal:food'])

    return df