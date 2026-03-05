
from collections import Counter
import re

def task_func(word: str) -> list:
    """
    Finds the most common two-letter combination in a given, cleaned word (lowercased and alphabetic characters only) and returns its frequency.
    The search is case-insensitive and ignores non-alphabetic characters.
    """
    # Clean the word by removing non-alphabetic characters and converting to lowercase
    clean_word = re.sub(r'[^a-zA-Z]', '', word.lower())

    # If the word has fewer than 2 letters, or after cleaning, has fewer than 2 alphabetic characters, return an empty list
    if len(clean_word) < 2 or len(clean_word) < 2:
        return []

    # Create a Counter object from the cleaned word
    counter = Counter(clean_word)

    # Get the most common two-letter combination and its frequency
    most_common = counter.most_common(2)

    # Return a list containing a single tuple with the most common two-letter combination and its frequency
    return [most_common]