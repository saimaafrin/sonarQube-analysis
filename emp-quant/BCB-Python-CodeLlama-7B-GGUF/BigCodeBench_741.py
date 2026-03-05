
from itertools import groupby
from operator import itemgetter

# Constants
KEY_FUNC = itemgetter(0)

def task_func(my_dict):
    aggregated_dict = {}
    for key, group in groupby(my_dict.items(), key=KEY_FUNC):
        values = [value for _, value in group]
        aggregated_dict[key] = sum(values)
    return aggregated_dict

print(task_func(my_dict))