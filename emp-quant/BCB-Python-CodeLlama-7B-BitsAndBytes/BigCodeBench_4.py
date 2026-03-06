
from collections import Counter
import itertools

def task_func(d):
    counts = Counter()
    for lst in d.values():
        counts.update(lst)
    return {k: counts[k] for k in counts}