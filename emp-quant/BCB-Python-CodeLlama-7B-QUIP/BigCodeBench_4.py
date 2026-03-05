
from collections import Counter
import itertools

def task_func(d):
    counter = Counter()
    for lst in itertools.chain(*d.values()):
        for i in lst:
            counter[i] += 1
    return counter