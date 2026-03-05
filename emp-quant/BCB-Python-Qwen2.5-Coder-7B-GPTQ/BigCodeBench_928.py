from collections import Counter
import itertools
import string
def task_func(word: str) -> dict:
    # Generate all possible two-letter combinations of the lowercase English alphabet
    alphabet = string.ascii_lowercase
    combinations = [''.join(p) for p in itertools.product(alphabet, repeat=2)]
    
    # Initialize a dictionary to store the frequency of each combination
    combination_counts = {combo: 0 for combo in combinations}
    
    # Count the frequency of each combination in the given word
    for combo in combinations:
        combination_counts[combo] = word.count(combo)
    
    return combination_counts