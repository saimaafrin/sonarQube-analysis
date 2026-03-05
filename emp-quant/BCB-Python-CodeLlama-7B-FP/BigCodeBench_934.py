from collections import Counter
import hashlib
def task_func(word: str) -> dict:
    """
    Count the occurrence of each adjacent pair of letters from left to right in a word and encode the result as an MD5 hash.
    """
    # Create a Counter object to count the occurrences of adjacent letter pairs
    counter = Counter()
    for i in range(len(word) - 1):
        counter[word[i] + word[i + 1]] += 1

    # Create a dictionary to store the counts
    counts = {}
    for pair, count in counter.items():
        counts[pair] = count

    # Encode the counts as an MD5 hash
    hash = hashlib.md5(str(counts).encode()).hexdigest()

    return counts