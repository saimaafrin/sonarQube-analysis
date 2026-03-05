
import random
from collections import Counter

def task_func(strings: list) -> dict:
    # Define the pattern to search for
    pattern = 'example'
    
    # Initialize a Counter to keep track of occurrences
    pattern_counter = Counter()
    
    # Iterate through each string in the list
    for string in strings:
        # Count occurrences of the pattern in the current string
        pattern_counter.update(string.split())
    
    # Return the dictionary with the count of the pattern
    return {pattern: pattern_counter[pattern] for pattern in pattern_counter}