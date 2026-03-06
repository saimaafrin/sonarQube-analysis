
import random
import string
import collections

# Constants
VALID_CHARACTERS = string.ascii_letters + string.digits

def task_func(n_strings, string_length):
    # Generate n random strings
    random_strings = [''.join(random.choices(VALID_CHARACTERS, k=string_length)) for _ in range(n_strings)]
    
    # Flatten the list of strings into a single string
    all_chars = ''.join(random_strings)
    
    # Count the frequency of each character
    char_count = collections.Counter(all_chars)
    
    return char_count