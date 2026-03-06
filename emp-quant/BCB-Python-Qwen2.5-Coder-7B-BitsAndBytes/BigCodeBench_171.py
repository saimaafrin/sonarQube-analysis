
import random
import pandas as pd
import collections

# Constants
VEGETABLES = ['Carrot', 'Potato', 'Tomato', 'Cabbage', 'Spinach']

def task_func(vegetable_dict, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Reverse the dictionary to map vegetables to people
    reversed_dict = {}
    for person, veggies in vegetable_dict.items():
        for veggie in veggies:
            if veggie not in reversed_dict:
                reversed_dict[veggie] = []
            reversed_dict[veggie].append(person)
    
    # Assign random counts to each vegetable
    vegetable_counts = {veggie: random.randint(1, 10) for veggie in reversed_dict}
    
    # Calculate the total count of all vegetables
    total_count = sum(vegetable_counts.values())
    
    # Calculate the percentage occurrence of each vegetable
    vegetable_percentages = {veggie: (count / total_count) * 100 for veggie, count in vegetable_counts.items()}
    
    # Create a DataFrame with vegetable names, their random counts, and their percentage occurrence
    data = {
        'Vegetable': list(vegetable_counts.keys()),
        'Count': list(vegetable_counts.values()),
        'Percentage': [f'{percentage:.2f}%' for percentage in vegetable_percentages.values()]
    }
    df = pd.DataFrame(data)
    
    return df

result_df = task_func(vegetable_dict)
print(result_df)