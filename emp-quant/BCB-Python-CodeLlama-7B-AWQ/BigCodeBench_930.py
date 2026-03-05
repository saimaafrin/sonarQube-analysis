import random
import string
POSSIBLE_LETTERS = ['a', 'b', 'c']
def task_func(word):
    """
    Generates a list of random pairs of adjacent letters from the given word.
    The number of such pairs will be equal to the length of the constant POSSIBLE_LETTERS.
    The function should raise the exception for: ValueError: If the input contains non-letter characters.
    The function should output with:
        list: A list of random pairs of adjacent letters from the word. If the word has fewer than 2 letters, returns a list of empty strings based on POSSIBLE_LETTERS length.
    """
    if not word.isalpha():
        raise ValueError("Input contains non-letter characters.")
    if len(word) < 2:
        return [""] * len(POSSIBLE_LETTERS)
    pairs = []
    for i in range(len(word) - 1):
        pairs.append((word[i], word[i + 1]))
    return pairs