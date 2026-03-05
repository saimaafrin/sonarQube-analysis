
import string
import random

BRACKETS = "(){}[]"

def task_func(length, random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
    return ''.join(random.choice(BRACKETS + string.ascii_lowercase) for _ in range(length))

string = task_func(34, random_seed=42)
print(string)

string = task_func(23, random_seed=1)
print(string)