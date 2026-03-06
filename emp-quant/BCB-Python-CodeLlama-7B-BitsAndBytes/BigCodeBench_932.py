
from collections import Counter
import re

def task_func(word: str) -> list:
    """
    Finds the most common two-letter combination in a given, cleaned word (lowercased and alphabetic characters only) and returns its frequency.
    The search is case-insensitive and ignores non-alphabetic characters.
    """
    # Clean the word by removing non-alphabetic characters and converting to lowercase
    clean_word = re.sub(r'[^a-zA-Z]', '', word.lower())

    # Create a Counter object to count the frequency of each two-letter combination
    counter = Counter(clean_word[i:i+2] for i in range(len(clean_word)-1))

    # Find the most common two-letter combination and its frequency
    most_common = counter.most_common(1)

    # Return a list containing a single tuple with the most common two-letter combination and its frequency
    return [most_common] if most_common else []