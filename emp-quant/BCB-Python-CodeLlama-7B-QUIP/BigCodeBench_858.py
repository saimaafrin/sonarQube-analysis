
import string
import random
from collections import Counter

def task_func(n, seed=None):
    if seed:
        random.seed(seed)
    random_letters = [random.choice(string.ascii_lowercase) for i in range(n)]
    return Counter(random_letters)