
from collections import defaultdict
import re

def task_func(word: str) -> dict:
    """
    Find the occurrences of each two-letter combination in the sanitized word, where only alphabetic characters are considered.
    :param word: The sanitized word to be analyzed
    :return: A dictionary with keys as two-letter combinations and values as their counts in the sanitized word
    """
    # Initialize the dictionary
    combinations = defaultdict(int)

    # Iterate over the characters in the word
    for i in range(len(word) - 1):
        # Get the current and next characters
        current = word[i]
        next = word[i + 1]

        # Check if the current and next characters are alphabetic
        if current.isalpha() and next.isalpha():
            # Add the combination to the dictionary
            combinations[current + next] += 1

    # Return the dictionary
    return combinations