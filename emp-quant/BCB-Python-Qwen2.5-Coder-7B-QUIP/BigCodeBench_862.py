
import random
import string
from collections import defaultdict

def task_func(n, seed=None):
    random.seed(seed)
    alphabet = list(string.ascii_lowercase)
    letter_dict = defaultdict(list)

    for _ in range(n):
        letter = random.choice(alphabet)
        letter_dict[letter].append(letter)

    return letter_dict