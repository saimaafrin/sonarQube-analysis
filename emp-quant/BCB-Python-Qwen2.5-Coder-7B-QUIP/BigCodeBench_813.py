
from itertools import combinations
import pandas as pd

def task_func(number_list, element):
    result = pd.DataFrame(columns=['Combinations'])
    for combo in combinations(number_list, 3):
        if sum(combo) == element:
            result = result.append(pd.DataFrame({'Combinations': [combo]}), ignore_index=True)
    return result