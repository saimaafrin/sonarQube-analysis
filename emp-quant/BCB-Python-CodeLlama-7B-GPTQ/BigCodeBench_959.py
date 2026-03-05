import string
import random
def task_func(text, seed=None):
    """
    Transforms the input text by replacing each alphabetic character with a random letter, while preserving the case and non-alphabetic characters of the original text.
    Notes:
    - Alphabet replacements are chosen from ascii characters of the same case as the original.
    - The function should output with:
        str: A transformed string with random letters replacing the alphabetic characters of the input text,
        preserving non-alphabetic characters and the original case.
    """
    if seed is not None:
        random.seed(seed)

    # Create a mapping of original characters to their corresponding random replacements
    char_map = {char: random.choice(string.ascii_letters) for char in string.ascii_letters}

    # Apply the mapping to the input text
    transformed_text = ''.join(char_map.get(char, char) for char in text)

    return transformed_text