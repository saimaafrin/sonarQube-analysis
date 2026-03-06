
from collections import defaultdict
import re

def task_func(word: str) -> dict:
    # Sanitize the word to keep only alphabetic characters
    sanitized_word = re.sub(r'[^a-zA-Z]', '', word)
    
    # Initialize a defaultdict to store the count of each two-letter combination
    two_letter_combinations = defaultdict(int)
    
    # Iterate over the sanitized word to find all two-letter combinations
    for i in range(len(sanitized_word) - 1):
        combination = sanitized_word[i:i+2]
        two_letter_combinations[combination] += 1
    
    return two_letter_combinations