
import pandas as pd
import itertools
import numpy as np

def task_func(animals=None, foods=None):
    # Define default lists if none are provided
    default_animals = ['Dog', 'Cat', 'Bird']
    default_foods = ['Fish', 'Meat', 'Grass']
    
    # Use default lists if input is None or empty
    if animals is None or len(animals) == 0:
        animals = default_animals
    if foods is None or len(foods) == 0:
        foods = default_foods
    
    # Generate all combinations of animals and foods
    combinations = list(itertools.product(animals, foods))
    
    # Shuffle the combinations to randomize the order
    np.random.shuffle(combinations)
    
    # Create a DataFrame from the combinations
    df = pd.DataFrame(combinations, columns=['Animal', 'Food'])
    
    return df