import pandas as pd
import itertools
import random
def task_func(colors, states):
    """
    Generates a pandas DataFrame containing shuffled combinations of provided colors and states.
    The DataFrame is formatted so that each column represents a series of unique combinations, with each combination displayed as "Color:State".
    Note that:
        - Cartesian product of 'colors' and 'states',
        - The number of columns in the resulting DataFrame is determined by the smaller number of elements in either the 'colors' or 'states' list,
        - Ensuring an even distribution without excess empty cells.
        - If the number of combinations is not evenly divisible by the number of columns, some columns will have fewer entries.
    """
    # Create a list of all possible combinations of colors and states
    all_combinations = list(itertools.product(colors, states))

    # Shuffle the list of combinations
    random.shuffle(all_combinations)

    # Create a DataFrame with the shuffled combinations
    df = pd.DataFrame(all_combinations, columns=['Color:State'])

    # Ensure that the number of columns is the lesser of the lengths of 'colors' and 'states'
    num_columns = min(len(colors), len(states))
    df = df.iloc[:, :num_columns]

    return df
colors = ['Red', 'Blue', 'Green']
states = ['California', 'Texas', 'Florida']