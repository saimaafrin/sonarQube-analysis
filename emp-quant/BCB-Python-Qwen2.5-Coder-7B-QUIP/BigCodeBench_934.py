
from collections import Counter
import hashlib

def task_func(word: str) -> dict:
    # Initialize a Counter to count occurrences of each adjacent pair
    pair_counter = Counter()

    # Iterate through the word and count each adjacent pair
    for i in range(len(word) - 1):
        pair = word[i] + word[i + 1]
        pair_counter[pair] += 1

    # Initialize an empty dictionary to store the result
    result = {}

    # Iterate through the items in the counter and encode each count as an MD5 hash
    for pair, count in pair_counter.items():
        result[pair] = hashlib.md5(str(count).encode()).hexdigest()

    return result