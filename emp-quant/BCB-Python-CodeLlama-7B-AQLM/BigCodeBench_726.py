import re
import random
from nltk.corpus import words
from random import sample
import nltk
SAMPLE_ENGLISH_WORDS = set(words.words())
def task_func(s, n):
    """
    Extract up to n different English words from a string, ignoring case. 
    The string is split into words and only the English words are retained.
    If there are fewer than n different English words, all distinct ones are returned.
    
    Parameters:
    - s (str): The string to extract words from.
    - n (int): The maximum number of different English words to extract.
    
    Returns:
    - List[str]: A list of up to n different English words found in the string.

    Requirements:
    - re
    - nltk
    - random
    
    Example:
    Given the nature of random sampling, the specific output can vary.
    >>> s = 'This is an example string with some random words: Apple, banana, Test, hello, world'
    >>> len(task_func(s, 5)) <= 5
    True
    >>> set(task_func("apple Apple APPle", 3)) == {"apple"}
    True
    """
    # Split the string into words
    words = re.split(r'\W+', s)
    # Remove empty strings
    words = [w for w in words if w]
    # Remove non-English words
    words = [w for w in words if w.lower() in SAMPLE_ENGLISH_WORDS]
    # Remove duplicates
    words = list(set(words))
    # Randomly sample up to n words
    return sample(words, min(n, len(words)))