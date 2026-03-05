
from collections import Counter
import itertools

def task_func(d):
    # Flatten the list of lists into a single list
    flattened_list = list(itertools.chain.from_iterable(d.values()))
    # Count the occurrences of each integer
    count_dict = Counter(flattened_list)
    return dict(count_dict)