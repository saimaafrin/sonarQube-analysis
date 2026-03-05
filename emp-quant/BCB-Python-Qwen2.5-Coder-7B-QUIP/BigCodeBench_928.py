
from collections import Counter
import itertools
import string

def task_func(word: str) -> dict:
    # Generate all possible two-letter combinations
    alphabet = string.ascii_lowercase
    combinations = list(itertools.combinations(alphabet, 2))
    
    # Initialize a dictionary with all combinations set to 0
    combination_dict = {combo: 0 for combo in combinations}
    
    # Count the occurrences of each combination in the word
    for i in range(len(word) - 1):
        combo = word[i:i+2]
        if combo in combination_dict:
            combination_dict[combo] += 1
    
    return combination_dict