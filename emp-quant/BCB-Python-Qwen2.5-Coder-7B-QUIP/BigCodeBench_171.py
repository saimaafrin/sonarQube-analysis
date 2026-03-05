
import random
import pandas as pd
import collections

# Constants
VEGETABLES = ['Carrot', 'Potato', 'Tomato', 'Cabbage', 'Spinach']

def task_func(vegetable_dict, seed=0):
    # Initialize the random seed for reproducibility
    random.seed(seed)

    # Reverse the dictionary to map vegetables to people
    people_dict = collections.defaultdict(list)
    for person, vegetable in vegetable_dict.items():
        people_dict[vegetable].append(person)

    # Assign random counts to each vegetable
    vegetable_counts = {vegetable: random.randint(1, 10) for vegetable in people_dict}

    # Calculate the total counts
    total_counts = sum(vegetable_counts.values())

    # Calculate the percentage occurrence of each vegetable
    vegetable_percentages = {vegetable: (count / total_counts) * 100 for vegetable, count in vegetable_counts.items()}

    # Create a DataFrame with the vegetable names, their random counts, and their percentage occurrence
    df = pd.DataFrame(list(vegetable_counts.items()), columns=['Vegetable', 'Count'])
    df['Percentage'] = df['Count'] / df['Count'].sum() * 100

    return df

result = task_func(vegetable_dict, seed=42)
print(result)