from collections import Counter
import hashlib
def task_func(word: str) -> dict:
    """
    Count the occurrence of each adjacent pair of letters from left to right in a word and encode the result as an MD5 hash.
    """
    # Create a Counter object to count the occurrences of adjacent letter pairs
    counter = Counter()

    # Iterate over the word and count the occurrences of adjacent letter pairs
    for i in range(len(word) - 1):
        pair = word[i] + word[i + 1]
        counter[pair] += 1

    # Create a dictionary with the counts of each adjacent letter pair
    counts = {pair: count for pair, count in counter.items()}

    # Encode the counts as an MD5 hash
    hash = hashlib.md5(str(counts).encode()).hexdigest()

    # Return the dictionary with the counts and the MD5 hash
    return {
        "counts": counts,
        "hash": hash,
    }