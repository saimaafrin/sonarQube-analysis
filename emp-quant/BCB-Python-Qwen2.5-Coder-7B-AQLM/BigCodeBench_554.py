
import numpy as np
import random

def task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL):
    def is_palindrome(sentence):
        return sentence == sentence[::-1]
    
    while True:
        num_words = np.random.randint(MIN_WORDS, MAX_WORDS + 1)
        words = random.sample(WORDS_POOL, num_words)
        sentence = ' '.join(words)
        if is_palindrome(sentence):
            return sentence