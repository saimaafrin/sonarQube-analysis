
import pandas as pd
import itertools
import random

def task_func(colors, states):
    # Generate a list of all possible combinations of colors and states
    all_combinations = list(itertools.product(colors, states))

    # Shuffle the list of combinations
    random.shuffle(all_combinations)

    # Create a DataFrame with the shuffled combinations
    df = pd.DataFrame(all_combinations, columns=['Color:State'])

    # Ensure that the number of columns is the lesser of the lengths of 'colors' and 'states'
    num_columns = min(len(colors), len(states))
    df = df.iloc[:, :num_columns]

    return df