from itertools import combinations
import pandas as pd
def task_func(number_list, element):
    # Check if the number_list is empty
    if not number_list:
        return pd.DataFrame(columns=['Combinations'])
    
    # Find all unique combinations of 3 numbers that add up to the element
    valid_combinations = [comb for comb in combinations(number_list, 3) if sum(comb) == element]
    
    # Create a DataFrame with the valid combinations
    result_df = pd.DataFrame(valid_combinations, columns=['Combinations'])
    
    return result_df