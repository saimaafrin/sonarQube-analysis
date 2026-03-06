
import random
import string
from collections import Counter

def task_func(num_strings, string_length):
    # Create a list of random strings
    strings = [random.choice(string.ascii_lowercase) for _ in range(num_strings)]

    # Flatten the list of strings into a single string
    flat_string = ''.join(strings)

    # Count the frequency of each character in the flat string
    char_counts = Counter(flat_string)

    # Sort the character counts by frequency in descending order
    sorted_counts = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

    # Return the sorted character counts as a list of tuples
    return sorted_counts