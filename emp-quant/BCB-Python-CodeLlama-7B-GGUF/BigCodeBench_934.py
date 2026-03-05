
from collections import Counter
import hashlib

def task_func(word: str) -> dict:
    """
    Count the occurrence of each adjacent pair of letters from left to right in a word and encode the result as an MD5 hash.
    :param word: The word to process.
    :return: A dictionary where keys are adjacent letter pairs and values are their counts.
    """
    # Create a Counter object to count the occurrences of adjacent pairs of letters
    counter = Counter(zip(word, word[1:]))

    # Convert the Counter object to a dictionary
    counts = dict(counter)

    # Encode the dictionary as an MD5 hash
    hash = hashlib.md5(str(counts).encode()).hexdigest()

    return counts