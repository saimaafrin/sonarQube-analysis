
import random
import string
import collections

# Constants
VALID_CHARACTERS = string.ascii_letters + string.digits

def task_func(n_strings, string_length):
    # Generate n random strings of the specified length
    random_strings = [''.join(random.choices(VALID_CHARACTERS, k=string_length) for _ in range(n_strings)]
    
    # Count the frequency of each character across all strings
    char_count = collections.Counter(''.join(random_strings))
    
    return char_count