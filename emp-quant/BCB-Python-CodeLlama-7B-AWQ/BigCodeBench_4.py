from collections import Counter
import itertools
def task_func(d):
    """
    Count the occurrence of each integer in the values of the input dictionary, where each value is a list of integers, and return a dictionary with these counts. The resulting dictionary's keys are the integers, and the values are their respective counts across all lists in the input dictionary.
    """
    counts = Counter()
    for values in d.values():
        counts.update(values)
    return counts
d = {
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': [7, 8, 9],
}