
import pandas as pd
import itertools
import numpy as np

def task_func(animals=None, foods=None):
    if animals is None or foods is None:
        return pd.DataFrame()
    if len(animals) == 0:
        animals = ['cat', 'dog', 'mouse']
    if len(foods) == 0:
        foods = ['apple', 'banana', 'orange']
    combinations = itertools.product(animals, foods)
    shuffled_combinations = np.random.permutation(combinations)
    df = pd.DataFrame(shuffled_combinations, columns=['animal', 'food'])
    return df