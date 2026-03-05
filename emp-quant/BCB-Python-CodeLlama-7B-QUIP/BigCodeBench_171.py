
import random
import pandas as pd
import collections
# Constants
VEGETABLES = ['Carrot', 'Potato', 'Tomato', 'Cabbage', 'Spinage']
def task_func(vegetable_dict, seed=0):
    # Reverse the dictionary to map vegetables to people
    vegetable_dict_reversed = {value: key for key, value in vegetable_dict.items()}
    # Assign random counts to vegetables
    vegetable_counts = {vegetable: random.randint(1, 10) for vegetable in VEGETABLES}
    # Calculate the occurrences of each vegetable as a percentage of the total counts
    vegetable_occurrences = {vegetable: vegetable_counts[vegetable] / sum(vegetable_counts.values()) for vegetable in VEGETABLES}
    # Create a DataFrame with the results
    df = pd.DataFrame({'Vegetable': VEGETABLES, 'Counts': vegetable_counts, 'Occurrences': vegetable_occurrences})
    return df