
from itertools import groupby
from operator import itemgetter

# Constants
KEY_FUNC = itemgetter(0)

def task_func(my_dict):
    aggregated_dict = {}
    for key, group in groupby(my_dict, key=KEY_FUNC):
        values = [value for key, value in group]
        aggregated_dict[key] = sum(values)
    return aggregated_dict

print(task_func(my_dict))