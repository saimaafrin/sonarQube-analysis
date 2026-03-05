
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
        letter_dict[letter] = [letter] * num_occurrences
    
    # Remove keys with empty lists
    letter_dict = {key: value for key, value in letter_dict.items() if value}
    
    return letter_dict