import re
from collections import Counter
def task_func(input_str):
    """
    Count the frequency of each alphanumeric character in a given string after removing all non-alphanumeric characters, treating uppercase and lowercase letters as the same.

    Args:
        input_str (str): The input string.

    Returns:
        dict: A dictionary with characters as keys (all lowercase) and their frequencies in the input string as values.
    """
    # Remove all non-alphanumeric characters from the input string
    clean_str = re.sub(r'[^a-zA-Z0-9]', '', input_str)

    # Convert the input string to lowercase
    lowercase_str = clean_str.lower()

    # Create a Counter object to count the frequency of each character in the lowercase string
    char_counter = Counter(lowercase_str)

    # Create a dictionary with the characters as keys and their frequencies as values
    char_freq_dict = {char: freq for char, freq in char_counter.items()}

    return char_freq_dict
input_str = "Hello, World!"