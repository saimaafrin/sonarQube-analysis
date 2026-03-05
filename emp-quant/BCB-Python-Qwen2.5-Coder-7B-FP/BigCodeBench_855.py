import random
import string
import collections
VALID_CHARACTERS = string.ascii_letters + string.digits
def task_func(n_strings, string_length):
    # Generate n random strings of the specified length
    random_strings = [''.join(random.choice(VALID_CHARACTERS) for _ in range(string_length)) for _ in range(n_strings)]
    
    # Concatenate all strings into one
    all_chars = ''.join(random_strings)
    
    # Count the frequency of each character
    char_frequency = collections.Counter(all_chars)
    
    return char_frequency