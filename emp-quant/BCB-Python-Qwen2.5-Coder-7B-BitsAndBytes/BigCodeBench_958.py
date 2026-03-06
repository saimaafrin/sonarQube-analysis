
import random
import re

def task_func(text, seed=None):
    if seed is not None:
        random.seed(seed)
    
    def scramble_word(word):
        if len(word) > 3:
            middle = list(word[1:-1])
            random.shuffle(middle)
            return word[0] + ''.join(middle) + word[-1]
        else:
            return word
    
    # Use regex to find all words and apply the scramble_word function
    scrambled_text = re.sub(r'\b\w+\b', scramble_word, text)
    return scrambled_text