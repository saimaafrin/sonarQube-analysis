
import random
import string
from collections import defaultdict

def task_func(n, seed=None):
    if seed is not None:
        random.seed(seed)
    
    result = defaultdict(list)
    letters = list(string.ascii_lowercase)
    
    for _ in range(n):
        letter = random.choice(letters)
        result[letter].append(letter)
    
    return result