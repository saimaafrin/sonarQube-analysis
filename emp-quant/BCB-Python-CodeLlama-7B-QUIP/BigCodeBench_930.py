
import random
import string
POSSIBLE_LETTERS = ['a', 'b', 'c']
def task_func(word):
    if not all(c in string.ascii_letters for c in word):
        raise ValueError("Input contains non-letter characters")
    if len(word) < 2:
        return ["" for i in range(len(POSSIBLE_LETTERS))]
    pairs = []
    for i in range(len(word) - 1):
        pairs.append(word[i] + word[i + 1])
    return pairs