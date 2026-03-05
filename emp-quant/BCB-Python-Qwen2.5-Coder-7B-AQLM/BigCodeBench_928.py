
from collections import Counter
import itertools
import string

def task_func(word: str) -> dict:
    # Generate all possible two-letter combinations of the lowercase English alphabet
    alphabet = string.ascii_lowercase
    combinations = [''.join(pair) for pair in itertools.product(alphabet, repeat=2)]
    
    # Initialize a dictionary with all combinations set to 0
    combination_counts = {combo: 0 for combo in combinations}
    
    # Count the frequency of each combination in the given word
    for combo in combinations:
        combination_counts[combo] = word.count(combo)
    
    return combination_counts