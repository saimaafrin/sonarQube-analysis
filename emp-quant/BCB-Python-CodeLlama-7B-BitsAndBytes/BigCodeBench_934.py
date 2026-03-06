
from collections import Counter
import hashlib

def task_func(word: str) -> dict:
    """
    Count the occurrence of each adjacent pair of letters from left to right in a word and encode the result as an MD5 hash.

    Args:
        word (str): The word to process.

    Returns:
        dict: A dictionary where keys are adjacent letter pairs and values are their counts.
    """
    # Create a Counter object to count the occurrences of each letter pair
    counter = Counter(zip(word, word[1:]))

    # Convert the Counter object to a dictionary
    letter_pairs = {(a, b): counter[(a, b)] for (a, b) in counter}

    # Encode the dictionary as an MD5 hash
    hash_object = hashlib.md5(str(letter_pairs).encode())
    hash_value = hash_object.hexdigest()

    return letter_pairs, hash_value