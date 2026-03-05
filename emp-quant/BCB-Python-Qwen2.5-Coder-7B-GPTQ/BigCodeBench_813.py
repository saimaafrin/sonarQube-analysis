from itertools import combinations
import pandas as pd
def task_func(number_list, element):
    # Generate all possible combinations of 3 numbers from the list
    all_combinations = list(combinations(number_list, 3))
    
    # Filter combinations that sum up to the given element
    valid_combinations = [comb for comb in all_combinations if sum(comb) == element]
    
    # Create a DataFrame with the valid combinations
    result_df = pd.DataFrame(valid_combinations, columns=['Combinations'])
    
    return result_df