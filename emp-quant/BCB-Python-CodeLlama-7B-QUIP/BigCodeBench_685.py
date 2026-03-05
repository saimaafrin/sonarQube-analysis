
from collections import Counter
from itertools import chain

def task_func(list_of_lists):
    return Counter(chain.from_iterable(list_of_lists))