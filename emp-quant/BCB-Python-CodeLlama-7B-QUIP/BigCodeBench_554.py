
import numpy as np
import random

def task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL):
    # Generate a random sentence of length between MIN_WORDS and MAX_WORDS
    sentence = " ".join(random.choice(WORDS_POOL) for _ in range(random.randint(MIN_WORDS, MAX_WORDS)))

    # Check if the sentence is a palindrome
    if sentence == sentence[::-1]:
        return sentence
    else:
        return "Invalid sentence"