from collections import Counter
import hashlib
def task_func(word: str) -> dict:
    # Create a dictionary to store the count of each adjacent pair
    pair_count = Counter()
    
    # Iterate over the word to count adjacent pairs
    for i in range(len(word) - 1):
        pair = word[i:i+2]
        pair_count[pair] += 1
    
    # Encode the result as an MD5 hash
    md5_hash = hashlib.md5(str(pair_count).encode()).hexdigest()
    
    return pair_count, md5_hash
word = "hello"