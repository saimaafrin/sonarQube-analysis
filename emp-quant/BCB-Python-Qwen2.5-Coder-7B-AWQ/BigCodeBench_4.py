from collections import Counter
import itertools
def task_func(d):
    # Flatten the list of lists into a single list
    flattened_list = list(itertools.chain.from_iterable(d.values()))
    # Count the occurrences of each integer in the flattened list
    count_dict = dict(Counter(flattened_list))
    return count_dict
d = {
    'a': [1, 2, 2, 3],
    'b': [2, 3, 4, 4, 4],
    'c': [5, 5, 6]
}