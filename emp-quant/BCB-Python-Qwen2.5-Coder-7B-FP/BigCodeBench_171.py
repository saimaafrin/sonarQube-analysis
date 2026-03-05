import random
import pandas as pd
import collections
def task_func(vegetable_dict, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Reverse the dictionary to map vegetables to people
    person_dict = collections.defaultdict(list)
    for person, vegetables in vegetable_dict.items():
        for vegetable in vegetables:
            person_dict[vegetable].append(person)
    
    # Assign random counts to each vegetable
    vegetable_counts = {vegetable: random.randint(1, 10) for vegetable in person_dict}
    
    # Calculate the total counts
    total_counts = sum(vegetable_counts.values())
    
    # Calculate the percentage occurrence of each vegetable
    vegetable_percentages = {vegetable: (count / total_counts) * 100 for vegetable, count in vegetable_counts.items()}
    
    # Create a DataFrame with vegetable names, their random counts, and their percentage occurrence
    result_df = pd.DataFrame({
        'Vegetable': list(vegetable_counts.keys()),
        'Count': list(vegetable_counts.values()),
        'Percentage': list(vegetable_percentages.values())
    })
    
    return result_df
vegetable_dict = {
    'Alice': ['Carrot', 'Potato'],
    'Bob': ['Tomato', 'Cabbage'],
    'Charlie': ['Spinach', 'Carrot', 'Tomato']
}