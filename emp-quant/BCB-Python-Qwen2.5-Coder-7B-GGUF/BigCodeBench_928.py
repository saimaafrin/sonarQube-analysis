
from collections import Counter
import itertools
import string

def task_func(word: str) -> dict:
    # Generate all possible two-letter combinations of the lowercase English alphabets
    all_combinations = [''.join(p) for p in itertools.product(string.ascii_lowercase, repeat=2)]
    
    # Initialize a dictionary with all combinations set to 0
    combination_count = {combo: 0 for combo in all_combinations}
    
    # Count the frequency of each combination in the given word
    for combo in all_combinations:
        combination_count[combo] = word.count(combo)
    
    return combination_count