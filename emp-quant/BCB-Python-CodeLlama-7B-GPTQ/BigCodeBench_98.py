import random
import string
from collections import Counter
def task_func(num_strings, string_length):
    """
    Creates a list of random strings, each of a specified length, and counts the frequency of each character across all strings.
    The function then returns the characters and their frequencies sorted by frequency in descending order.
    The random strings are composed of ASCII lowercase characters.
    """
    # Generate a list of random strings
    random_strings = [
        ''.join(random.choice(string.ascii_lowercase) for _ in range(string_length))
        for _ in range(num_strings)
    ]

    # Count the frequency of each character in all strings
    char_freq = Counter()
    for s in random_strings:
        for c in s:
            char_freq[c] += 1

    # Sort the characters by frequency in descending order
    sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

    # Return the list of tuples
    return sorted_chars
num_strings = 100
string_length = 10
random_strings = [
    ''.join(random.choice(string.ascii_lowercase) for _ in range(string_length))
    for _ in range(num_strings)
]
char_freq = Counter()
sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)