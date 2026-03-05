import pandas as pd
import itertools
import random
def task_func(colors, states):
    """
    Generates a pandas DataFrame containing shuffled combinations of provided colors and states.
    The DataFrame is formatted so that each column represents a series of unique combinations,
    with each combination displayed as "Color:State".
    Note that:
        - Cartesian product of 'colors' and 'states'
        - The number of columns in the resulting DataFrame is determined by the smaller number of elements in either the 'colors' or 'states' list,
          ensuring an even distribution without excess empty cells.
        - If the number of combinations is not evenly divisible by the number of columns, some columns will have fewer entries.
    """
    # Generate Cartesian product of colors and states
    combinations = list(itertools.product(colors, states))

    # Shuffle the combinations
    random.shuffle(combinations)

    # Create DataFrame with each combination as a string
    df = pd.DataFrame(combinations, columns=['Color:State'])

    # Distribute combinations across columns
    num_columns = min(len(colors), len(states))
    df = df.T.groupby(df.index // num_columns).apply(lambda x: x.tolist()).T

    return df
colors = ['red', 'green', 'blue']
states = ['CA', 'NY', 'TX']