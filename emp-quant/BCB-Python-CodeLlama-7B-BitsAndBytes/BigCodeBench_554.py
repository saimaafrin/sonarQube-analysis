
import numpy as np
import random

def task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL):
    # Generate a random sentence with a length between MIN_WORDS and MAX_WORDS
    sentence_length = np.random.randint(MIN_WORDS, MAX_WORDS)
    sentence = ' '.join(random.choice(WORDS_POOL) for _ in range(sentence_length))

    # Check if the sentence is a palindrome
    if sentence == sentence[::-1]:
        return sentence
    else:
        return 'Invalid sentence'

sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
print(sentence)