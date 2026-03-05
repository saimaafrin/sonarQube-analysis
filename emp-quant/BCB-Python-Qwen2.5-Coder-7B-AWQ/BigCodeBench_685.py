from collections import Counter
from itertools import chain
def task_func(list_of_lists):
    # Merge all sublists into a single list
    merged_list = list(chain.from_iterable(list_of_lists))
    # Count the occurrences of each element in the merged list
    element_count = Counter(merged_list)
    return element_count