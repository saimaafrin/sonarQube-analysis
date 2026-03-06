
from itertools import combinations
import pandas as pd

def task_func(number_list, element):
    if not number_list:
        return pd.DataFrame(columns=['Combinations'])
    
    valid_combinations = [comb for comb in combinations(number_list, 3) if sum(comb) == element]
    
    if not valid_combinations:
        return pd.DataFrame(columns=['Combinations'])
    
    result_df = pd.DataFrame(valid_combinations, columns=['Combinations'])
    return result_df