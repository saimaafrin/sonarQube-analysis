
import re
from collections import Counter

def task_func(input_str):
    # Remove all non-alphanumeric characters from the input string
    clean_str = re.sub(r'[^a-zA-Z0-9]', '', input_str)

    # Convert the clean string to lowercase
    lowercase_str = clean_str.lower()

    # Create a Counter object to count the frequency of each character
    char_counter = Counter(lowercase_str)

    # Create a dictionary with characters as keys and their frequencies as values
    char_freq_dict = {char: freq for char, freq in char_counter.items()}

    return char_freq_dict