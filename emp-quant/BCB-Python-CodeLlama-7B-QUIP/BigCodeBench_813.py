
from itertools import combinations
import pandas as pd

def task_func(number_list, element):
    if not number_list:
        return pd.DataFrame(columns=['Combinations'])
    combinations = []
    for i in range(len(number_list)):
        for j in range(i + 1, len(number_list)):
            for k in range(j + 1, len(number_list)):
                if number_list[i] + number_list[j] + number_list[k] == element:
                    combinations.append((number_list[i], number_list[j], number_list[k]))
    return pd.DataFrame(combinations, columns=['Combinations'])