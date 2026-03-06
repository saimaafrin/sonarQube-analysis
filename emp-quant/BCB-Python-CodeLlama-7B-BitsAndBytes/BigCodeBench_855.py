
import random
import string
import collections

# Constants
VALID_CHARACTERS = string.ascii_letters + string.digits

def task_func(n_strings, string_length):
    # Generate n random strings of specified length
    random_strings = [random.choice(VALID_CHARACTERS) for _ in range(n_strings)]

    # Count the frequency of each character across all strings
    char_counts = collections.Counter(c for s in random_strings for c in s)

    # Return the result as a dictionary
    return {c: char_counts[c] for c in char_counts}