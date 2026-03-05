from itertools import combinations
import pandas as pd
def task_func(number_list, element):
    # Check if the number_list is empty
    if not number_list:
        return pd.DataFrame(columns=['Combinations'])
    
    # Find all unique combinations of 3 numbers
    comb = combinations(number_list, 3)
    
    # Filter combinations that add up to the element
    valid_combinations = [c for c in comb if sum(c) == element]
    
    # Create a DataFrame with the valid combinations
    result_df = pd.DataFrame(valid_combinations, columns=['Combinations'])
    
    return result_df