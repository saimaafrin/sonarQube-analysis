import random
import re
def task_func(text, seed=None):
    """
    Scramble the letters in each word of a given text, keeping the first and last letters of each word intact.
    """
    if seed is not None:
        random.seed(seed)
    words = re.findall(r'\b\w+\b', text)
    scrambled_words = []
    for word in words:
        if len(word) <= 3:
            scrambled_words.append(word)
        else:
            scrambled_words.append(''.join(random.sample(word, len(word))))
    return ' '.join(scrambled_words)