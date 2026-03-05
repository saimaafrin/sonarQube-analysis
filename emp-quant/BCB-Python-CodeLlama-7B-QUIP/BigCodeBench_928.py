
from collections import Counter
import itertools
import string

def task_func(word: str) -> dict:
    # Create a dictionary to store the counts
    counts = {}

    # Iterate over the word and create a counter for each two-letter combination
    for i in range(len(word) - 1):
        for j in range(i + 1, len(word)):
            combination = word[i:j + 1]
            counts[combination] = counts.get(combination, 0) + 1

    # Return the dictionary
    return counts