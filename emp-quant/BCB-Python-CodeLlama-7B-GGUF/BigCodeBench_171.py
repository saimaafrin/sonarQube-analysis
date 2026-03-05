
import random
import pandas as pd
import collections

# Constants
VEGETABLES = ['Carrot', 'Potato', 'Tomato', 'Cabbage', 'Spinach']

def task_func(vegetable_dict, seed=0):
    # Reverse the dictionary to map vegetables to people
    vegetable_to_people = {vegetable: [] for vegetable in VEGETABLES}
    for person, vegetables in vegetable_dict.items():
        for vegetable in vegetables:
            vegetable_to_people[vegetable].append(person)

    # Assign random counts to vegetables
    random.seed(seed)
    vegetable_counts = {vegetable: random.randint(1, 10) for vegetable in VEGETABLES}

    # Calculate percentage occurrence of each vegetable
    vegetable_occurrences = {vegetable: (count / sum(vegetable_counts.values())) * 100 for vegetable, count in vegetable_counts.items()}

    # Create DataFrame
    df = pd.DataFrame(data=vegetable_occurrences, index=VEGETABLES, columns=['Percentage Occurrence'])
    df['Vegetable'] = df.index
    df['People'] = [', '.join(vegetable_to_people[vegetable]) for vegetable in VEGETABLES]

    return df