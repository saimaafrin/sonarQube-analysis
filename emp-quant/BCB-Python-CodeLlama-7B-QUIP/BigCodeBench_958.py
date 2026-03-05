
import random
import re

def task_func(text, seed=None):
    words = re.split(r'\W+', text)
    for i in range(len(words)):
        word = words[i]
        if len(word) > 3:
            scrambled_word = ''.join(random.choice(word) for i in range(len(word)))
            words[i] = scrambled_word
    return ' '.join(words)