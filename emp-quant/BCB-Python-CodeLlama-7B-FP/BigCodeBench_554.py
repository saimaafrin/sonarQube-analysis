import numpy as np
import random
def task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL):
    """
    Generates a palindrome sentence using random words from a specified pool.
    The sentence's length is randomly chosen between a minimum (MIN_WORDS) and maximum (MAX_WORDS) number of words.
    The function ensures that the sentence reads the same forwards and backwards.
    Check if the generated sentence length is within the specified range.
    >>> sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    >>> MIN_WORDS <= len(sentence.split()) <= MAX_WORDS
    True
    """
    # Generate a random sentence length between MIN_WORDS and MAX_WORDS
    sentence_length = np.random.randint(MIN_WORDS, MAX_WORDS)

    # Generate a random sentence using the WORDS_POOL
    sentence = ' '.join(random.choice(WORDS_POOL) for _ in range(sentence_length))

    # Check if the sentence is a palindrome
    if sentence == sentence[::-1]:
        return sentence
    else:
        return task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
MIN_WORDS = 5
MAX_WORDS = 10
WORDS_POOL = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'orange', 'peach', 'pineapple', 'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon']