
import random
import string
POSSIBLE_LETTERS = ['a', 'b', 'c']

def task_func(word):
    if not all(char in string.ascii_letters for char in word):
        raise ValueError("Input contains non-letter characters.")
    
    if len(word) < 2:
        return [''] * len(POSSIBLE_LETTERS)
    
    adjacent_pairs = [word[i:i+2] for i in range(len(word) - 1)]
    
    return adjacent_pairs