
from collections import Counter
import itertools
import string

def task_func(word: str) -> dict:
    """
    Returns a dictionary containing all possible two-letter combinations of the lowercase English alphabets.
    The dictionary values represent the frequency of these two-letter combinations in the given word.
    If a combination does not appear in the word, its value will be 0.
    """
    alphabet = string.ascii_lowercase
    combinations = itertools.product(alphabet, repeat=2)
    counts = Counter(combinations)
    for combination in counts:
        if combination not in word:
            counts[combination] = 0
    return counts