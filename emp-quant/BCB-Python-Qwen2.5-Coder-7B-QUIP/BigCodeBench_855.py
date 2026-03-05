
import random
import string
import collections

# Constants
VALID_CHARACTERS = string.ascii_letters + string.digits

def task_func(n_strings, string_length):
    # Generate n random strings of the specified length
    random_strings = [''.join(random.choices(VALID_CHARACTERS, k=string_length)) for _ in range(n_strings)]
    
    # Initialize a Counter to count character frequencies
    char_count = collections.Counter()
    
    # Count the frequency of each character across all strings
    for string in random_strings:
        char_count.update(string)
    
    # Return the dictionary of character frequencies
    return dict(char_count)