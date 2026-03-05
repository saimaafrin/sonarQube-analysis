from itertools import combinations
import pandas as pd
def task_func(number_list, element):
    """
    Find all unique combinations of 3 numbers from a list that add up to a certain element.
    If the number_list is empty, or there is no combination that adds up to the element, an empty dataframe is returned.
    """
    if not number_list:
        return pd.DataFrame(columns=['Combinations'])

    combinations_list = []
    for i in range(len(number_list)):
        for j in range(i + 1, len(number_list)):
            for k in range(j + 1, len(number_list)):
                if number_list[i] + number_list[j] + number_list[k] == element:
                    combinations_list.append((number_list[i], number_list[j], number_list[k]))

    if not combinations_list:
        return pd.DataFrame(columns=['Combinations'])

    return pd.DataFrame(combinations_list, columns=['Combinations'])