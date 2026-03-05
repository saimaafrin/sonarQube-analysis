
import random
import string
from collections import defaultdict

def task_func(n, seed=None):
    if seed is not None:
        random.seed(seed)

    alphabet = string.ascii_lowercase
    letter_dict = defaultdict(list)

    for letter in alphabet:
        num_occurrences = random.randint(0, n)
        for _ in range(num_occurrences):
            letter_dict[letter].append(letter)

    return letter_dict