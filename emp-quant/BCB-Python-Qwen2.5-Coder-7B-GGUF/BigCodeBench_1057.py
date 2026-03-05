
import pandas as pd
import itertools
import numpy as np

def task_func(animals=None, foods=None):
    # Define default lists if not provided
    default_animals = ['Lion', 'Tiger', 'Bear']
    default_foods = ['Meat', 'Fish', 'Vegetables']
    
    # Use default lists if provided lists are empty or None
    animals = animals if animals and animals else default_animals
    foods = foods if foods and foods else default_foods
    
    # Generate all combinations of animals and foods
    combinations = list(itertools.product(animals, foods))
    
    # Shuffle the combinations to randomize the DataFrame layout
    np.random.shuffle(combinations)
    
    # Create a DataFrame from the shuffled combinations
    df = pd.DataFrame(combinations, columns=['animal:food'])
    
    return df