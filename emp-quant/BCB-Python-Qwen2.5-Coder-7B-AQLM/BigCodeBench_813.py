
from itertools import combinations
import pandas as pd

def task_func(number_list, element):
    if not number_list:
        return pd.DataFrame(columns=['Combinations'])
    
    result = []
    for combo in combinations(number_list, 3):
        if sum(combo) == element:
            result.append(combo)
    
    if not result:
        return pd.DataFrame(columns=['Combinations'])
    
    return pd.DataFrame(result, columns=['Combinations'])