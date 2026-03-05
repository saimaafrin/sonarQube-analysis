
import random
import string

# Constants
LETTERS = string.ascii_letters

def task_func(num_words, word_length):
    if num_words < 0 or word_length < 0:
        raise ValueError("Invalid input")
    words = []
    for i in range(num_words):
        word = ''.join(random.choice(LETTERS) for i in range(word_length))
        words.append(word)
    return words