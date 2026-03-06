
import random
import string

POSSIBLE_LETTERS = ['a', 'b', 'c']

def task_func(word):
    if not all(char in string.ascii_letters for char in word):
        raise ValueError("Input contains non-letter characters.")

    pairs = []
    for i in range(len(word) - 1):
        pairs.append((word[i], word[i + 1]))

    return pairs