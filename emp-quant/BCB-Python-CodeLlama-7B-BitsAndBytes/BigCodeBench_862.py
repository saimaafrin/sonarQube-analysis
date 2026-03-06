
import random
import string
from collections import defaultdict

def task_func(n, seed=None):
    if seed is not None:
        random.seed(seed)
    alphabet = string.ascii_lowercase
    letter_dict = defaultdict(list)
    for i in range(n):
        letter = random.choice(alphabet)
        letter_dict[letter].append(letter)
    return letter_dict

print(task_func(30, seed=1))