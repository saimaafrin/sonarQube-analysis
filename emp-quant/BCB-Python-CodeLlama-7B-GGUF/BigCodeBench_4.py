
from collections import Counter
import itertools

def task_func(d):
    counts = Counter()
    for lst in itertools.chain.from_iterable(d.values()):
        counts.update(lst)
    return dict(counts)