
import string
import random

def task_func(length, random_seed=None):
    if random_seed:
        random.seed(random_seed)
    str = ''
    for i in range(length):
        str += random.choice(string.BRACKETS)
    return str