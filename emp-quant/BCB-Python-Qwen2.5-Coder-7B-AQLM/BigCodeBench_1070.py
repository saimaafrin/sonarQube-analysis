
import pandas as pd
from random import shuffle

# Constants
POSSIBLE_VALUES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def task_func(list_of_lists):
    dfs = []
    for sublist in list_of_lists:
        # Shuffle the possible values
        shuffled_values = POSSIBLE_VALUES[:]
        shuffle(shuffled_values)
        # Create a DataFrame with columns named as per the sublist
        df = pd.DataFrame({col: shuffled_values for col in sublist})
        dfs.append(df)
    return dfs