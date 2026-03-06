
from itertools import combinations
import pandas as pd

def task_func(number_list, element):
    if not number_list:
        return pd.DataFrame(columns=['Combinations'])

    combinations_list = []
    for i in range(len(number_list)):
        for j in range(i+1, len(number_list)):
            for k in range(j+1, len(number_list)):
                if number_list[i] + number_list[j] + number_list[k] == element:
                    combinations_list.append((number_list[i], number_list[j], number_list[k]))

    return pd.DataFrame(combinations_list, columns=['Combinations'])

result = task_func([-1, 1, 0, -2, 2, 3], 0)
print(result)

result = task_func([], 0)
print(result)