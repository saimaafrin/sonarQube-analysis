
import pandas as pd
import itertools
import numpy as np

def task_func(animals=None, foods=None):
    # Define default lists if not provided
    default_animals = ['Lion', 'Tiger', 'Bear']
    default_foods = ['Meat', 'Fish', 'Vegetables']
    
    # Use default lists if provided lists are None or empty
    if animals is None or not animals:
        animals = default_animals
    if foods is None or not foods:
        foods = default_foods
    
    # Generate all combinations of animals and foods
    combinations = list(itertools.product(animals, foods))
    
    # Shuffle the combinations to ensure randomness
    np.random.shuffle(combinations)
    
    # Create a DataFrame from the combinations
    df = pd.DataFrame(combinations, columns=['animal:food'])
    
    return df