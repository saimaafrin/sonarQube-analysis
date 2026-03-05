
import string
import random

def task_func(text, seed=None):
    """
    Transforms the input text by replacing each alphabetic character with a random letter, while preserving the case and non-alphabetic characters of the original text.
    """
    if seed is not None:
        random.seed(seed)

    # Create a mapping of original characters to random characters
    char_map = {}
    for char in text:
        if char.isalpha():
            # Get the original character and its case
            orig_char = char.lower()
            orig_case = char.isupper()

            # Get a random character of the same case
            rand_char = random.choice(string.ascii_letters).lower()
            if orig_case:
                rand_char = rand_char.upper()

            # Add the mapping to the dictionary
            char_map[orig_char] = rand_char

    # Replace the characters in the input text with the mapped characters
    transformed_text = text
    for orig_char, rand_char in char_map.items():
        transformed_text = transformed_text.replace(orig_char, rand_char)

    return transformed_text