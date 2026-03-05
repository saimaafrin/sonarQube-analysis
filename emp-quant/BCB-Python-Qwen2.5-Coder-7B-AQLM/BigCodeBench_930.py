
import random
import string

POSSIBLE_LETTERS = ['a', 'b', 'c']

def task_func(word):
    # Check if the input contains non-letter characters
    if not word.isalpha():
        raise ValueError("Input contains non-letter characters")
    
    # If the word has fewer than 2 letters, return a list of empty strings
    if len(word) < 2:
        return [''] * len(POSSIBLE_LETTERS)
    
    # Generate a list of random pairs of adjacent letters
    pairs = []
    for i in range(len(word) - 1):
        pairs.append(word[i:i+2])
    
    # Shuffle the pairs
    random.shuffle(pairs)
    
    # Return the first 'len(POSSIBLE_LETTERS)' pairs
    return pairs[:len(POSSIBLE_LETTERS)]