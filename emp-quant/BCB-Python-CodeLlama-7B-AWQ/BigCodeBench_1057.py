import pandas as pd
import itertools
import numpy as np
def task_func(animals=None, foods=None):
    """
    Create a DataFrame with combinations of animals and foods in a 'animal:food' format.
    Handling of Special Cases:
    - If both 'animals' and 'foods' lists are empty or not provided, the function returns an empty DataFrame.
    - If either 'animals' or 'foods' list is empty or not provided, the function uses its predefined list for the missing parameter.
    """
    # Predefined lists of animals and foods
    animals = ['cat', 'dog', 'bird', 'fish']
    foods = ['apple', 'banana', 'orange', 'carrot']

    # Check if either list is empty or not provided
    if not animals or not foods:
        return pd.DataFrame()

    # Generate all possible combinations of animals and foods
    combinations = list(itertools.product(animals, foods))

    # Shuffle the combinations randomly
    np.random.shuffle(combinations)

    # Create a DataFrame with each row representing a unique animal and each column representing a food item
    df = pd.DataFrame(combinations, columns=['animal', 'food'])

    # Convert the 'animal' and 'food' columns to strings
    df['animal'] = df['animal'].astype(str)
    df['food'] = df['food'].astype(str)

    # Return the DataFrame
    return df