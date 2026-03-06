import random
import string
LETTERS = string.ascii_letters
def task_func(num_words, word_length):
    """
    Create a list of random words of a certain length.

    Parameters:
    - num_words (int): The number of words to generate.
    - word_length (int): The length of each word.

    Returns:
    - words (list): A list of random words.

    Requirements:
    - random
    - string

    Raises:
    - ValueError: If num_words or word_length is negative.
    
    Example:
    >>> task_func(5, 3)
    ['Ohb', 'Vrp', 'oiV', 'gRV', 'IfL']
    """
    if num_words < 0:
        raise ValueError("num_words must be positive")
    if word_length < 0:
        raise ValueError("word_length must be positive")

    words = []
    for i in range(num_words):
        word = ''
        for j in range(word_length):
            word += random.choice(LETTERS)
        words.append(word)
    return words