import random
import re
def task_func(text, seed=None):
    if seed is not None:
        random.seed(seed)
    
    def scramble_word(word):
        if len(word) > 3:
            middle_chars = list(word[1:-1])
            random.shuffle(middle_chars)
            return word[0] + ''.join(middle_chars) + word[-1]
        return word
    
    # Use regex to find words and scramble them
    scrambled_text = re.sub(r'\b\w+\b', scramble_word, text)
    return scrambled_text