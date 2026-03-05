
import random
import string
from collections import Counter

def task_func(num_strings, string_length):
    # Generate a list of random strings
    random_strings = [random_string(string_length) for i in range(num_strings)]

    # Count the frequency of each character in the strings
    char_counts = Counter(random_strings)

    # Sort the counts in descending order
    sorted_counts = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

    # Return the sorted counts
    return sorted_counts

def random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))