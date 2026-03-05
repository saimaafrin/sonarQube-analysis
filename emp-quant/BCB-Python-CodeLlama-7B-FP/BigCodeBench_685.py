from collections import Counter
from itertools import chain
def task_func(list_of_lists):
    """
    Merge all sublists from a list of lists into a list and return a count of the elements.
    """
    merged_list = list(chain.from_iterable(list_of_lists))
    return Counter(merged_list)
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]