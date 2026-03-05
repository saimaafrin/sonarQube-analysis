import string
import random
def task_func(text, seed=None):
    """
    Transforms the input text by replacing each alphabetic character with a random letter, while preserving the case and non-alphabetic characters of the original text.
    Notes:
    - Alphabet replacements are chosen from ASCII characters of the same case as the original.
    - The function should output with:
        - str: A transformed string with random letters replacing the alphabetic characters of the input text,
        - preserving non-alphabetic characters and the original case.
    """
    if seed is not None:
        random.seed(seed)

    # Create a mapping of original characters to their corresponding random replacements
    char_map = {}
    for char in string.ascii_letters:
        if char.isalpha():
            char_map[char] = chr(random.randint(ord(char), ord(char) + 25))

    # Apply the mapping to the input text
    output = ""
    for char in text:
        if char.isalpha():
            output += char_map[char]
        else:
            output += char

    return output