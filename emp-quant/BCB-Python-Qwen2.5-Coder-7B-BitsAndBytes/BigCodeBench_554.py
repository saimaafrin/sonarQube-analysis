
import numpy as np
import random

def task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL):
    def is_palindrome(s):
        return s == s[::-1]

    while True:
        num_words = random.randint(MIN_WORDS, MAX_WORDS)
        words = random.sample(WORDS_POOL, num_words)
        sentence = ' '.join(words)
        reversed_sentence = ' '.join(reversed(words))
        candidate_sentence = f"{sentence} {reversed_sentence}"
        
        if is_palindrome(candidate_sentence.replace(' ', '')):
            return candidate_sentence