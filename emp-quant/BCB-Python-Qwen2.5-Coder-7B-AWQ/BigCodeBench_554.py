import numpy as np
import random
def task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL):
    """
    Generates a palindrome sentence using random words from a specified pool.
    The sentence's length is randomly chosen between a minimum (MIN_WORDS) and maximum (MAX_WORDS) number of words.
    The function ensures that the sentence reads the same forwards and backwards.
    
    Parameters:
    MIN_WORDS (int): Minimum number of words in the sentence.
    MAX_WORDS (int): Maximum number of words in the sentence.
    WORDS_POOL (list): List of words to choose from.
    
    Returns:
    str: The generated palindrome sentence.
    """
    # Ensure the range is valid
    if MIN_WORDS > MAX_WORDS:
        raise ValueError("MIN_WORDS must be less than or equal to MAX_WORDS")
    
    # Randomly choose the number of words in the sentence
    num_words = np.random.randint(MIN_WORDS, MAX_WORDS + 1)
    
    # Select random words from the pool
    words = random.sample(WORDS_POOL, num_words)
    
    # Create the palindrome sentence
    sentence = ' '.join(words)
    reversed_sentence = ' '.join(reversed(words))
    palindrome_sentence = f"{sentence} {reversed_sentence}"
    
    return palindrome_sentence
MIN_WORDS = 3
MAX_WORDS = 5
WORDS_POOL = ["apple", "banana", "cherry", "date", "elderberry"]