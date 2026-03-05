import re
from collections import Counter
def task_func(input_str):
    """
    Count the frequency of each alphanumeric character in a given string after removing all non-alphanumeric characters, treating uppercase and lowercase letters as the same.
    :param input_str: The input string.
    :return: A dictionary with characters as keys (all lowercase) and their frequencies in the input string as values.
    """
    # Remove all non-alphanumeric characters from the input string
    clean_str = re.sub(r'[^a-zA-Z0-9]', '', input_str)

    # Convert the input string to lowercase
    lower_str = clean_str.lower()

    # Create a Counter object to count the frequency of each character in the input string
    char_counter = Counter(lower_str)

    # Return the Counter object as a dictionary
    return char_counter
input_str = "Hello, World!"