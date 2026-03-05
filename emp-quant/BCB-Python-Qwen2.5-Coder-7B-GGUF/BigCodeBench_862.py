
import random
import string
from collections import defaultdict

def task_func(n, seed=None):
    if seed is not None:
        random.seed(seed)
    
    letter_dict = defaultdict(list)
    letters = string.ascii_lowercase
    
    for _ in range(n):
        letter = random.choice(letters)
        letter_dict[letter].append(letter)
    
    return letter_dict