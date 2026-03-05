
import random
import string
from collections import defaultdict

def task_func(n, seed=None):
    if seed:
        random.seed(seed)
    result = defaultdict(list)
    for i in range(n):
        result[chr(random.randint(97, 123))].append(chr(random.randint(97, 123)))
    return result