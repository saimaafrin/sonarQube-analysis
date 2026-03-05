import numpy as np
import random
def task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL):
    # Helper function to check if a sentence is a palindrome
    def is_palindrome(sentence):
        return sentence == sentence[::-1]
    
    # Generate a random number of words within the specified range
    num_words = np.random.randint(MIN_WORDS, MAX_WORDS + 1)
    
    # Randomly select words from the pool to form a sentence
    words = random.sample(WORDS_POOL, num_words)
    sentence = ' '.join(words)
    
    # Ensure the sentence is a palindrome
    while not is_palindrome(sentence):
        words = random.sample(WORDS_POOL, num_words)
        sentence = ' '.join(words)
    
    return sentence
MIN_WORDS = 3
MAX_WORDS = 5
WORDS_POOL = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]