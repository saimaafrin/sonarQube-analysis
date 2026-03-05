
import collections
import string
import random

def task_func(length, seed=0):
    random.seed(seed)
    random_string = ''.join(random.choices(string.ascii_letters, k=length))
    frequency = collections.Counter(random_string)
    return frequency