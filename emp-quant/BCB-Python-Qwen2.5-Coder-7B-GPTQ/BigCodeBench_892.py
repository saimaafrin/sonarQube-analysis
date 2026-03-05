import random
from collections import Counter
def task_func(strings: list) -> dict:
    pattern = 'a'  # Define the pattern to search for
    pattern_count = Counter(string.count(pattern) for string in strings)
    return dict(pattern_count)
strings = ['apple', 'banana', 'cherry', 'date', 'elderberry']