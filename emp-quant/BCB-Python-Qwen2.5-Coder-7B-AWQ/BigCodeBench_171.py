import random
import pandas as pd
import collections
def task_func(vegetable_dict, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Reverse the dictionary to map vegetables to people
    person_dict = {person: [veg for veg in vegetables if veg in vegetable_dict[person]] for person in vegetable_dict}
    
    # Flatten the list of vegetables and count occurrences
    all_vegetables = [veg for sublist in person_dict.values() for veg in sublist]
    vegetable_counts = collections.Counter(all_vegetables)
    
    # Assign random counts to each vegetable
    random_counts = {veg: random.randint(1, 10) for veg in vegetable_counts}
    
    # Calculate the total count of random counts
    total_count = sum(random_counts.values())
    
    # Calculate the percentage occurrence of each vegetable
    percentage_occurrence = {veg: (count / total_count) * 100 for veg, count in random_counts.items()}
    
    # Create a DataFrame with the results
    result_df = pd.DataFrame({
        'Vegetable': list(random_counts.keys()),
        'Random Count': list(random_counts.values()),
        'Percentage Occurrence': list(percentage_occurrence.values())
    })
    
    return result_df