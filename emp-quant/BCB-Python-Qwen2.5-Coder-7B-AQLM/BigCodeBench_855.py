
import random
import string
import collections

# Constants
VALID_CHARACTERS = string.ascii_letters + string.digits

def task_func(n_strings, string_length):
    # Initialize a counter to keep track of character frequencies
    char_counter = collections.Counter()
    
    # Generate n random strings and update the counter
    for _ in range(n_strings):
        random_string = ''.join(random.choices(VALID_CHARACTERS, k=string_length))
        char_counter.update(random_string)
    
    # Convert the counter to a dictionary and return
    return dict(char_counter)