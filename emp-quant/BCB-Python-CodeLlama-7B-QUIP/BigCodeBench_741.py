
from itertools import groupby
from operator import itemgetter

# Constants
KEY_FUNC = itemgetter(0)

def task_func(my_dict):
    aggregated_dict = {}
    for key, group in groupby(my_dict, KEY_FUNC):
        aggregated_dict[key] = sum(group)
    return aggregated_dict