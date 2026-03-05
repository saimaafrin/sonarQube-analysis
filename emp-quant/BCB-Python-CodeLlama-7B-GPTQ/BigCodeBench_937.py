import re
from collections import Counter
def task_func(input_str):
    """
    Count the frequency of each alphanumeric character in a given string after removing all non-alphanumeric characters, treating uppercase and lowercase letters as the same.
    The function should output with:
        dict: A dictionary with characters as keys (all lowercase) and their frequencies in the input string as values.
    """
    # Remove all non-alphanumeric characters from the input string
    input_str = re.sub(r'[^a-zA-Z0-9]', '', input_str)

    # Convert the input string to lowercase
    input_str = input_str.lower()

    # Create a Counter object to count the frequency of each character
    counter = Counter(input_str)

    # Create a dictionary with the characters as keys and their frequencies as values
    char_freq_dict = {char: freq for char, freq in counter.items()}

    return char_freq_dict