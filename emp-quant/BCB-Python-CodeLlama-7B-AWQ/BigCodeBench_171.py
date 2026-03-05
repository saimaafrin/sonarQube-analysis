import random
import pandas as pd
import collections
VEGETABLES = ['Carrot', 'Potato', 'Tomato', 'Cabbage', 'Spinach']
def task_func(vegetable_dict, seed=0):
    """
    Calculate statistics for the vegetables preferred by people listed in the input dictionary.
    The function reverses the dictionary to map vegetables to people and assigns random counts to these vegetables.
    It then calculates the occurrences of each vegetable as a percentage of the total counts.
    A dictionary is created to map each vegetable to a person from the input where vegetables are values.
    Random counts between 1 and 10 are assigned to simulate varying popularity or availability of each vegetable.
    """
    # Reverse the dictionary to map vegetables to people
    people_dict = {value: key for key, value in vegetable_dict.items()}

    # Assign random counts to vegetables
    random.seed(seed)
    vegetable_counts = {vegetable: random.randint(1, 10) for vegetable in VEGETABLES}

    # Calculate percentage occurrence of each vegetable
    total_counts = sum(vegetable_counts.values())
    vegetable_percentages = {vegetable: (count / total_counts) * 100 for vegetable, count in vegetable_counts.items()}

    # Create DataFrame with columns for vegetable names, their random counts, and their percentage occurrence within the total counts
    df = pd.DataFrame(data={'Vegetable': VEGETABLES, 'Random Counts': list(vegetable_counts.values()), 'Percentage Occurrence': list(vegetable_percentages.values())})

    return df
vegetable_dict = {'Alice': 'Carrot', 'Bob': 'Potato', 'Charlie': 'Tomato', 'David': 'Cabbage', 'Eve': 'Spinach'}