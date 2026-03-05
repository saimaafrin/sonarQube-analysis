
from collections import Counter
import hashlib

def task_func(word: str) -> dict:
    # Create a dictionary to store the count of each adjacent letter pair
    pair_counts = Counter()
    
    # Iterate over the word and count each adjacent pair
    for i in range(len(word) - 1):
        pair = word[i:i+2]
        pair_counts[pair] += 1
    
    # Encode the result as an MD5 hash
    md5_hash = hashlib.md5(str(pair_counts).encode()).hexdigest()
    
    # Return the dictionary and the MD5 hash
    return pair_counts, md5_hash