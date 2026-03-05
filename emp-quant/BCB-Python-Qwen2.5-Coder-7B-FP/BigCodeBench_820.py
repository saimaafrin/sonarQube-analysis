import random
import string
LETTERS = string.ascii_letters
def task_func(num_words, word_length):
    """
    Generate a list of random words of a specified length.

    Args:
        num_words (int): The number of words to generate.
        word_length (int): The length of each word.

    Returns:
        words (list): A list of random words.

    Raises:
        ValueError: If num_words or word_length is negative.
    """
    if num_words < 0 or word_length < 0:
        raise ValueError("num_words and word_length must be non-negative integers.")
    
    words = [''.join(random.choice(LETTERS) for _ in range(word_length)) for _ in range(num_words)]
    return words