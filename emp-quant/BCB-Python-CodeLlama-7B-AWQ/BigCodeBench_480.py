import re
import random
import pandas as pd
def task_func(data_list, seed=None):
    """
    Shuffle the substrings within each string in a given list.
    This function takes a list of comma-separated strings and splits each into substrings.
    It extracts substrings based on commas, removing leading and trailing whitespaces from each.
    Then, it shuffles these processed substrings within each string, and returns a pandas DataFrame with two columns: "Original String" and "Shuffled String".
    """
    # Set random seed if provided
    if seed is not None:
        random.seed(seed)

    # Create a list of tuples with original and shuffled strings
    data = [(original, ''.join(random.sample(substring.split(','), len(substring.split(','))))) for original, substring in data_list]

    # Create a pandas DataFrame with the data
    df = pd.DataFrame(data, columns=['Original String', 'Shuffled String'])

    return df
data_list = [
    'apple, banana, cherry',
    'orange, lemon, lime',
    'grape, strawberry, watermelon'
]