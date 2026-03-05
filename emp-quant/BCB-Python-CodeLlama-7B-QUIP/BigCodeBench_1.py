
import collections
import random
import string

def task_func(length=100):
    if length < 0:
        raise ValueError("Length must be a positive number")
    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    char_counts = collections.Counter(random_string)
    return char_counts