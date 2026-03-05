
from collections import Counter
import hashlib

def task_func(word: str) -> dict:
    counter = Counter()
    for i in range(len(word) - 1):
        counter[word[i] + word[i + 1]] += 1
    return counter
    return hashlib.md5(str(counter).encode()).hexdigest()