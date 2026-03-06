
from collections import Counter
import hashlib

def task_func(word: str) -> dict:
    # Create a list of adjacent letter pairs
    pairs = [word[i:i+2] for i in range(len(word)-1)]
    
    # Count occurrences of each pair
    pair_counts = Counter(pairs)
    
    # Encode the result as an MD5 hash
    md5_hash = hashlib.md5(str(pair_counts).encode()).hexdigest()
    
    return pair_counts, md5_hash